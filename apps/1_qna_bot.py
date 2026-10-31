import os
from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter
import streamlit as st
# Look for .env in the parent directory
load_dotenv(dotenv_path="../.env")

# openrouter/free automatically picks an available, responsive free model
llm = ChatOpenRouter(model="openrouter/free")

# while True:
#     query = input("User: ")
#     if query.lower() in ["quit","exit","bye"]:
#         print("GoodBye ")
#         break
#     res = llm.invoke(query)
#     print("AI: ",res.content,"\n")

st.title("AskBuddy - AI QnA Bot")
st.markdown("My QnA Bot with LangChain and Free Model !")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)

query = st.chat_input("Ask anything ?")
if query:
    st.session_state.messages.append({"role":"user","content":query})
    st.chat_message("user").markdown(query)
    res = llm.invoke(query)
    st.chat_message("ai").markdown(res.content)
    st.session_state.messages.append({"role":"ai","content":res.content})