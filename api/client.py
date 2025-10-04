import requests
import streamlit as st

def get_openai_response(input_text):
    response=requests.post("http://localhost:8000/gpt/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']['content']

def get_ollama_response(input_text):
    response=requests.post(
    "http://localhost:8000/llm/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']

    ## streamlit framework

st.title('Langchain Demo With LLAMA2 API')
input_text=st.text_input("Write an essay on")
if input_text:
    col1, col2 = st.columns(2)
    with col1:
        st.write("**OpenAI GPT-3.5-turbo Response**")
        st.write(get_openai_response(input_text))
    with col2:
        st.write("**Ollama LLaMA2 Response**")
        st.write(get_ollama_response(input_text))