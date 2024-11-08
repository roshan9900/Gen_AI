import streamlit as st 
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai 
import os 
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

def get_response(question):
    response = chat.send_message(question,stream=True)
    return response

st.set_page_config(page_title="Q and A Demo")
st.header("gemini llm app")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input('input',key='input')
submit = st.button('ask any question')
if submit and input:
    response = get_response(input)
    st.session_state['chat_history'].append(("you",input))
    st.subheader('the repsonse is ')
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(('bot',chunk.text))
        
st.subheader('the chat history is ')
for role, text in st.session_state['chat_history']:
    st.write(f'{role}: {text}')