import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Sameed.core", page_icon="🤖")

st.title("🤖 Sameed.core")
st.write("Official AI Avatar of Sameed | Data Analyst")
st.markdown("---")

# STEP 1: Apni Nayi API Key yahan quotes ke beech daalein
API_KEY = "AIzaSyApCEXfY-bjHlC7fFLtD2dVPUer8FT4YPQ"

try:
    genai.configure(api_key=API_KEY)
    
    # Naya model format jo 2026 mein standard hai
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

        # Chatbot ka response
        response = model.generate_content(f"You are Sameed's AI assistant. Answer briefly: {prompt}")
        
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})

except Exception as e:
    # Isse humein pata chalega exactly kya error hai
    st.error(f"Opps! Dikkat yahan hai: {e}")
