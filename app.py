import streamlit as st
from PyPDF2 import PdfReader
import ollama

st.set_page_config(page_title="AI PDF Chatbot")

st.title("🤖 AI PDF Chatbot")

uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file:

    pdf_reader = PdfReader(uploaded_file)

    text = ""

    for page in pdf_reader.pages:
        text += page.extract_text()

    st.success("PDF uploaded successfully!")

    question = st.text_input("Ask a question about the PDF")

    if question:

        prompt = f"""
        You are an AI assistant.

        Use the following PDF content to answer the user's question.

        PDF CONTENT:
        ----------------
        {text}
        ---------------

        USER QUESTION:
        {question}

        Give a clear answer based only on the PDF.
        """


        response = ollama.chat(
            model='llama3',
            messages=[
                {
                    'role': 'user',
                    'content': prompt
                }
            ]
        )

        answer = response['message']['content']

        st.subheader("Answer")
        st.write(answer)