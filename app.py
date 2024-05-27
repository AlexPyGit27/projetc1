import openai
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

openai.api_key ="sk-proj-7HxgmVGvIkfBiZXbjgDmT3BlbkFJllGIBwF8grzkm52iNF9V"

st.markdown("<h1 style='text-align: center;'>salexGPT</h1>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hola, soy salexGPT, ¿En qué puedo ayudarte?"}]

for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])

if user_input := st.chat_input():
    st.session_state["messages"].append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=st.session_state["messages"]
    )
    responseMessage = response['choices'][0]['message']['content']
    st.session_state["messages"].append({"role": "assistant", "content": responseMessage})
    st.chat_message("assistant").write(responseMessage)
   