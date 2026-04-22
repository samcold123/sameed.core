import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Sameed.core", page_icon="🤖")
st.title("🤖 Sameed.core")
st.write("Official AI Avatar of Sameed | Data Analyst")

# API Key setup
genai.configure(api_key="AIzaSyDhMsoji0XAx4nYcDBE6UdNhrDbXxj2Woc")

# Yahan 'models/' lagana zaroori hai
model = genai.GenerativeModel('models/gemini-1.5-flash')

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me anything!"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        # Simple prompt
        response = model.generate_content(f"You are Sameed's AI. Answer: {prompt}")
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"Error: {e}")
