# Q&A Chatbot with Hugging Face
from langchain import HuggingFaceHub

#from dotenv import load_dotenv
#load_dotenv()  # take environment variables from .env.

import streamlit as st
import os

os.environ["HUGGINGFACEHUB_API_TOKEN"]="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"

## Function to load OpenAI model and get respones
def get_openai_response(question):
    llm_huggingface=HuggingFaceHub(repo_id="google/flan-t5-large",model_kwargs={"temperature":0,"max_length":64})
    response=llm_huggingface(question)
    return response

##initialize our streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Langchain Application")

input=st.text_input("Input: ",key="input")
response=get_openai_response(input)

submit=st.button("Ask the question")

## If ask button is clicked
if submit:
    st.subheader("The Response is")
    st.write(response)


## streamlit app
st.set_page_config("Chat With Multiple PDF")
st.header("Chat with Multiple PDF using Gemini :books:")

user_question = st.text_input("Ask a Question from the PDF Files")

if user_question:
    user_input(user_question)

with st.sidebar:
    st.title("Menu:")
    pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
    if st.button("Submit & Process"):
        with st.spinner("Processing..."):
            raw_text = get_pdf_text(pdf_docs)
            text_chunks = get_text_chunks(raw_text)
            get_vector_store(text_chunks)
            st.success("Done")

footer = """
---
#### Made By [Surat Banerjee](https://www.linkedin.com/in/surat-banerjee/)
For Any Queries, Reach out on [Portfolio](https://suratbanerjee.wixsite.com/myportfoliods)  
"""

st.markdown(footer, unsafe_allow_html=True)

