# Q&A Chatbot with Gemini
import streamlit as st
import os, random, time
import google.generativeai as genai
from IPython.display import display
# from IPython.display import Markdown
# import pathlib
# import textwrap

#Gemini Key
os.environ['GOOGLE_API_KEY']="AIzaSyB6-jZLBXeOeLFBhFaU11oidwAeBATkrds"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

st.set_page_config(page_title="Q&A Demo")
st.header("🎊 SURAT Q&A ChatBot 🫰")

if "history" not in st.session_state:
    st.session_state.history = []

model = genai.GenerativeModel('gemini-1.5-pro')
chat = model.start_chat(history = st.session_state.history)

with st.sidebar:
    if st.button("Clear Chat Window", use_container_width=True, type="primary"):
        st.session_state.history = []
        st.rerun()

for message in chat.history:
    role ="assistant" if message.role == 'model' else message.role
    with st.chat_message(role):
        st.markdown(message.parts[0].text)

if prompt := st.chat_input(""):
    prompt = prompt.replace('\n', ' \n')
    with st.chat_message("user"):st.markdown(prompt)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("Thinking...")
        try:
            full_response = ""
            for chunk in chat.send_message(prompt, stream=True):
                word_count = 0
                random_int = random.randint(5,10)
                for word in chunk.text:
                    full_response+=word
                    word_count+=1
                    if word_count == random_int:
                        time.sleep(0.05)
                        message_placeholder.markdown(full_response + "_")
                        word_count = 0
                        random_int = random.randint(5,10)
            message_placeholder.markdown(full_response)
        except genai.types.generation_types.BlockedPromptException as e:st.exception(e)
        except Exception as e:st.exception(e)
        st.session_state.history = chat.history


