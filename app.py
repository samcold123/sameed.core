import streamlit as st
import google.generativeai as genai

# Page ki settings
st.set_page_config(page_title="Sameed.core", page_icon="🤖")

# Interface ka header
st.title("🤖 Sameed.core")
st.markdown("---")
st.write("Official AI Avatar of Sameed | Data Analyst | SQL Developer")

# API Key Setup - Is line mein apni key daal dena
# Example: genai.configure(api_key="AIzaSy...")
genai.configure(api_key="AIzaSyDhMsoji0XAx4nYcDBE6UdNhrDbXxj2Woc")

# Model selection
model = genai.GenerativeModel('gemini-1.5-flash')

# Chat history maintain karne ke liye
if "messages" not in st.session_state:
    st.session_state.messages = []

# Purani baatein dikhane ke liye
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input box
if prompt := st.chat_input("Sameed.core se kuch puchiye..."):
    # User ka message save aur display karna
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        # AI ko instruct karna ki woh aapka avatar hai
        persona = (
            "Your name is Sameed.core. You are the digital twin of Sameed. "
            "Sameed is a Data Analyst from Chikodi, Karnataka. "
            "He has an 'A' grade in Data Analytics from Fusion Software Institute, Pune. "
            "Respond helpfully and professionally in the user's language (Hindi/English)."
        )
        
        # AI se jawab mangna
        response = model.generate_content(f"{persona}\n\nUser Question: {prompt}")
        
        # Jawab display aur save karna
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
        
    except Exception as e:
        st.error(f"Technical Error: {e}")
