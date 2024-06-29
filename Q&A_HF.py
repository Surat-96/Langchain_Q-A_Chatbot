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

footer = """
---
#### Made By [Surat Banerjee](https://www.linkedin.com/in/surat-banerjee/)
For Any Queries, Reach out on [Portfolio](https://suratbanerjee.wixsite.com/myportfoliods)  
"""

st.markdown(footer, unsafe_allow_html=True)

