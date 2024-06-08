import streamlit as st
import requests
from PyPDF2 import PdfReader
from io import BytesIO

# Function to extract text from PDF
@st.cache_data
def extract_data(pdf_file, language):
    files = {"file": (pdf_file.name, pdf_file, "application/pdf")}
    response = requests.post("http://127.0.0.1:5000/process_pdf", files=files)
    if response.status_code == 200:
        full_text = response.json()
        full_text = full_text['full_text']
    else:
        full_text = 'Couldn\'t fetch data. Try again... :('
    return full_text


def answer_question(text, question):
    if question:
        st.write("QUESTION ASKED")
        response = requests.post("http://127.0.0.1:5000/ask_question", json={"question": question})
        if response.status_code == 200:
            answer = response.json().get("answer")
            st.write("Answer:")
            st.write(answer)
        else:
            st.write("Error:")
            st.write(response.json().get("error", "Unknown error"))
    else:
        st.write("Please enter a question.")
    return f"Your question was: {question}\n"

# Greeting and PDF upload
st.title("DeepLogic Document CHATBOT")
st.write("Hello! I am your chatbot. Please upload your invoice in PDF file and select a language.")

pdf_file = st.file_uploader("Upload your PDF", type=["pdf"])
language = st.selectbox("Select Language", ["English", "Spanish", "French", "German"])

if pdf_file and language:
    with st.spinner('Processing PDF...'):
        pdf_text = extract_data(pdf_file, language)
        st.success("PDF uploaded and processed successfully!")
        st.write("Extracted Text:")
        st.write(pdf_text[:2000])

        st.write("Now you can ask questions about the PDF content.")
        user_question = st.text_input("Ask your question from the given pdf : ")
    
        if user_question:
            with st.spinner('Answering your question...'):
                response = answer_question(pdf_text, user_question)
                st.write(response)
