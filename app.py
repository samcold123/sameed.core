import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Sameed.core", page_icon="🤖")

st.title("🤖 Sameed.core")
st.write("Official AI Avatar of Sameed | Data Analyst")

# STEP 1: Apni Nayi API Key yahan quotes ke beech daalein
API_KEY = "AIzaSyDISnUx63cMAb-o-aiY1TsNlXxV2lwnY5w"

genai.configure(api_key=API_KEY)

# STEP 2: Naya model naam (Jo error nahi dega)
model = genai.GenerativeModel('gemini-1.5-flash-latest')

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Sameed.core se puchiye..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        # Simple response generation
        response = model.generate_content(f"You are Sameed's AI assistant. Answer: {prompt}")
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"Error: {e}")
