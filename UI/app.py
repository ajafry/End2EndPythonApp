from dotenv import load_dotenv
import os
import streamlit as st
import pandas as pd
import requests

load_dotenv()  # Load environment variables from .env file

st.title('Azure Container Apps')
st.subheader('Using Microservices from a web application')

firstNumber = st.number_input('Enter the first number', value=0)
secondNumber = st.number_input('Enter the second number', value=0)

addURL = os.getenv('ADD_API')
multiplyURL = os.getenv('MULTIPLY_API')
subtractURL = os.getenv('SUBTRACT_API')

# Create three columns
col1, col2, col3 = st.columns(3)

def callAPI(url):
    response = requests.get(url)
    return response.json()

def addNumbers():
    url = f'{addURL}/{firstNumber}/{secondNumber}'
    with st.status(f'Calling API at {url}', expanded=True):
        st.write(callAPI(url))

def subtractNumbers():
    url = f'{subtractURL}/{firstNumber}/{secondNumber}'
    with st.status(f'Calling API at {url}', expanded=True):
        st.write(callAPI(url))

def multiplyNumbers():
    url = f'{multiplyURL}/{firstNumber}/{secondNumber}'
    with st.status(f'Calling API at {url}', expanded=True):
        st.write(callAPI(url))

# Add buttons to each column
with col1:
    st.button("Add", use_container_width=True, on_click=addNumbers)
with col2:
    st.button("Subtract", use_container_width=True, on_click=subtractNumbers)
with col3:
    st.button("Multiply", use_container_width=True, on_click=multiplyNumbers)