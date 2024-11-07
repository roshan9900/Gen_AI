import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai
import os


genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

try: 
    model = genai.GenerativeModel('gemini-pro')
    def get_reponse(question):
        response = model.generate_content(question)
        return response.text

    st.set_page_config(page_title="Q and A App")
    st.header("LLM App for Question and Answering")
    input = st.text_input('input',key='input')
    submit = st.button("Ask the question")

    if submit:
        response = get_reponse(input)
        st.write(response)
except Exception as e:
    print(e)

    
