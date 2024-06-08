from langchain_community.vectorstores import Chroma
from langchain_community import embeddings
from langchain_community.llms import Ollama
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.text_splitter import CharacterTextSplitter

# Initialize the local model
model_local = Ollama(model="llama3")

def process_input(question):
    # Example invoice text
    invoice_text = """
                    12345 Papierfeld Deutschland Tel. (0123) 4567 Fax (0123) 4568 info@kraxi.com www.kraxi.com

                    Kraxi GmbH - Flugzeugallee 17 - 12345 Papierfeld - Deutschland Papierflieger-Vertriebs-GmbH Helga Musterfrau Rabattstr. 25 34567 Osterhausen Deutschland Rechnungsnummer: 2019-03 Liefer- und Rechnungsdatum: 8. Mai 2019 Kundennummer: 987-654 Ihre Auftragsnummer: ABC-123 Beträge in EUR

                    Pos. Artikelbeschreibung Menge Preis Betrag
                    1 Superdrachen 2 20,00 40,00
                    2 Turbo Flyer 5 40,00 200,00
                    3 Sturzflug-Geier 1 180,00 180,00
                    4 Eisvogel 3 50,00 150,00
                    5 Storch 10 20,00 200,00
                    6 Adler 1 75,00 75,00
                    7 Kostenlose Zugabe 1 0,00 0,00
                    Rechnungssumme netto 845,00
                    zuzüglich 19% MwSt. 160,55
                    Rechnungssumme brutto 1.005,55
                    Zahlbar innerhalb von 30 Tagen netto auf unser Konto. Bitte geben Sie dabei die Rechnungsnummer an. Skontoabzüge werden nicht akzeptiert.
                    """

    # Split the text into chunks
    text_splitter = CharacterTextSplitter.from_tiktoken_encoder(chunk_size=500, chunk_overlap=50)
    doc_splits = text_splitter.split_text(invoice_text)
    
    # Convert text chunks into embeddings and store in vector database
    vectorstore = Chroma.from_texts(
        texts=doc_splits,
        collection_name="rag-chroma",
        embedding=embeddings.OllamaEmbeddings(model='nomic-embed-text'),
    )
    retriever = vectorstore.as_retriever()
    
    # Perform the RAG 
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

