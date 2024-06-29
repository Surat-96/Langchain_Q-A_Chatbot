# Q&A Chatbot with OpenAI
from langchain.llms import OpenAI

#from dotenv import load_dotenv
#load_dotenv()  # take environment variables from .env.

import streamlit as st
import os

os.environ["OPEN_API_KEY"]="sk-HBcNcxp8X8oAKhSGT3BlbkFJ9sHkCuOITYjONfcc0Y3p"
## Function to load OpenAI model and get respones
def get_openai_response(question):
    llm=OpenAI(openai_api_key=os.environ["OPEN_API_KEY"],model_name="text-davinci-003",temperature=0.6)
    response=llm(question)
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



