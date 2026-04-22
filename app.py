import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Sameed.core", page_icon="🤖")
st.title("🤖 Sameed.core")
st.write("Official AI Avatar of Sameed | Data Analyst")

# STEP 1: Apni NAYI KEY yahan quotes ke beech daalein
API_KEY = "AIzaSyCQzKQApXNGdwY8PdpC1BEiZvvGC6G3j5Q"

# Forcefully bypassing v1beta error using 'rest' transport
genai.configure(api_key=API_KEY, transport='rest')

# Using the most stable model name
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
        # Instruction for the AI
        persona = "You are Sameed.core, a Data Analyst from Chikodi. Answer the user."
        response = model.generate_content(f"{persona}\n\nUser: {prompt}")
        
        if response.text:
            with st.chat_message("assistant"):
                st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"Error: {e}")
