import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Sameed.core", page_icon="🤖")
st.title("🤖 Sameed.core")
st.write("Official AI Avatar of Sameed | Data Analyst | Chikodi")

# API Key setup
genai.configure(api_key="AIzaSyDhMsoji0XAx4nYcDBE6UdNhrDbXxj2Woc")
model = genai.GenerativeModel('gemini-1.5-flash')

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask Sameed.core..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    persona = "Your name is Sameed.core. You are Sameed's AI twin. Sameed is a Data Analyst from Chikodi, Karnataka. Respond in the user's language (Hindi/English)."
    response = model.generate_content(f"{persona}\\n\\nUser: {prompt}")
    
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
