import streamlit as st
import google.generativeai as genai

# Page Configuration
st.set_page_config(page_title="Sameed.core", page_icon="🤖")
st.title("🤖 Sameed.core")
st.write("Official AI Avatar of Sameed | Data Analyst")
st.markdown("---")

# --- STEP 1: API KEY DAALEIN ---
# Jo key aapne AI Studio se copy ki hai, use niche " " ke beech mein paste karein
API_KEY = "AIzaSyCPi9p85tm0sLrHlyOgovIbOFShpqKIJAQ"

try:
    genai.configure(api_key=API_KEY)
    # 1.5 flash agar 404 de raha hai, toh hum seedha 'gemini-pro' use karenge
    model = genai.GenerativeModel('gemini-pro')
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Sameed.core se kuch puchiye..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # AI ko batana ki woh kaun hai
        persona = "You are Sameed.core, the AI twin of Sameed, a Data Analyst from Chikodi. Answer briefly."
        response = model.generate_content(f"{persona}\n\nUser: {prompt}")
        
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})

except Exception as e:
    st.error(f"Technical Error: {e}")
    st.info("Sameed bhai, agar abhi bhi 404 aa raha hai, toh iska matlab API Key active nahi hui hai.")
