import streamlit as st 
import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))


model = genai.GenerativeModel('gemini-pro-vision')

def response(input, image):
    if input !="":
        re = model.generate_content([input,image])
    else:
        re = model.generate_content(image)
    return re.text

st.set_page_config('gemini vision appli')
st.header('fdsklj')
input = st.text_input('input',key='input')
submit = st.button('ask question')

uploaded_file = st.file_uploader('choose an image to upload',type=['jpg','jpge','png'])
image = ''
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='uploaded image',use_column_width=True)
    
submit = st.button('tell me about the image')
if submit:
    res = response(input, image)

    st.subheader('the response is ')
    st.write(res)  

    