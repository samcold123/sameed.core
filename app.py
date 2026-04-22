import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Sameed.core", page_icon="🤖")

st.title("🤖 Sameed.core")
st.write("Official AI Avatar of Sameed | Data Analyst")

# STEP 1: Apni NAYI KEY yahan quotes ke beech daalein
API_KEY = "AIzaSyApCEXfY-bjHlC7fFLtD2dVPUer8FT4YPQ"

# Forcefully configuring the latest API version
genai.configure(api_key=API_KEY)

# Use 'gemini-1.5-flash' directly without the 'models/' prefix
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
        persona = "You are Sameed.core, a Data Analyst from Chikodi. Help the user."
        response = model.generate_content(f"{persona}\n\nUser: {prompt}")
        
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"Error logic update: {e}")
