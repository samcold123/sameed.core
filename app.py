import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Sameed.core", page_icon="🤖")
st.title("🤖 Sameed.core")
st.write("Official AI Avatar of Sameed | Data Analyst")

# STEP: Apni NAYI KEY yahan paste karein
API_KEY = "AIzaSyApCEXfY-bjHlC7fFLtD2dVPUer8FT4YPQ"

# Google ko batana ki humein purana v1beta nahi chahiye
genai.configure(api_key=API_KEY, transport='rest')

# Naya model select karne ka sahi tarika
model = genai.GenerativeModel('gemini-1.5-flash')

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
        # Response mangne ka tarika
        response = model.generate_content(prompt)
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"Dikkat yahan hai: {e}")
