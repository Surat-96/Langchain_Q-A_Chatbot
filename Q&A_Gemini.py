# Q&A Chatbot with Gemini
#from langchain.llms import OpenAI

import streamlit as st
import os
import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown

#Gemini Key
os.environ['GOOGLE_API_KEY']="AIzaSyB6-jZLBXeOeLFBhFaU11oidwAeBATkrds"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

## Function to load OpenAI model and get respones
def get_gemini_response(question):
    #model = genai.GenerativeModel('gemini-pro')
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content(question)
    return response.text

##initialize our streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("🎊 Q&A ChatBot 🫰")
input=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")

## If ask button is clicked
if submit:
    response=get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)

footer = """
---
#### Made By [Surat Banerjee](https://www.linkedin.com/in/surat-banerjee/)
For Any Queries, Reach out on [Portfolio](https://suratbanerjee.wixsite.com/myportfoliods)  
"""

st.markdown(footer, unsafe_allow_html=True)
