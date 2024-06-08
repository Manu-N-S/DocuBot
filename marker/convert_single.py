import os
import tempfile
from flask import Flask, request, jsonify
import pypdfium2
from marker.convert import convert_single_pdf
from marker.logger import configure_logging
from marker.models import load_all_models

from langchain_community.vectorstores import Chroma
from langchain_community import embeddings
from langchain_community.llms import Ollama
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.text_splitter import CharacterTextSplitter



# Configure logging and load models
configure_logging()
model_lst = load_all_models()
model_local = Ollama(model="llama3")
retriever = None

def create_embedding(invoice_text):
    # Split the text into chunks
    text_splitter = CharacterTextSplitter.from_tiktoken_encoder(chunk_size=7500, chunk_overlap=100)
    doc_splits = text_splitter.split_text(invoice_text)
    
    # Convert text chunks into embeddings and store in vector database
    vectorstore = Chroma.from_texts(
        texts=doc_splits,
        collection_name="rag-chroma",
        embedding=embeddings.OllamaEmbeddings(model='nomic-embed-text'),
    )
    retriever = vectorstore.as_retriever()
    return retriever

def perform_rag(retriever,question):
    after_rag_template = """ This is an reciept of purchase , Answer the question based only on the following context:
    {context}
    Question: {question}
    """
    after_rag_prompt = ChatPromptTemplate.from_template(after_rag_template)
    after_rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | after_rag_prompt
        | model_local
        | StrOutputParser()
    )
    return after_rag_chain.invoke(question)


app = Flask(__name__)

@app.route('/ask_question',methods=['POST'])
def process_question():
    global retriever
    qn = request.json
    qn = qn['question'] 
    answer = perform_rag(retriever,qn)

    return jsonify({"answer": answer})


@app.route('/process_pdf', methods=['POST'])
def process_pdf():
    global retriever
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file and file.filename.endswith('.pdf'):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file_path = temp_file.name
            file.save('demo.pdf')
        
        full_text, images, out_meta = convert_single_pdf('demo.pdf', model_lst, max_pages=1, langs=['German'], batch_multiplier=2, start_page=None)
        retriever = create_embedding(full_text)
        print("Vector Embedding Created.")
        return jsonify({"full_text": full_text})
    else:
        return jsonify({"error": "Invalid file type"}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
