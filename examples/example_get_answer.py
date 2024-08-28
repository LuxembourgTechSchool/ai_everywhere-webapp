import streamlit as st
from proxy import lts_proxy

prompt = st.chat_input("Write your prompt for chat completion")

if prompt:
    proxy = lts_proxy.Proxy()
    role = "You're an helpful assistant"
    answer = proxy.get_answer(role, prompt)
    st.write(answer)
