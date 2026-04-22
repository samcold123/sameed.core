import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Sameed.core", page_icon="🤖")
st.title("🤖 Sameed.core")
st.write("Official AI Avatar of Sameed | Data Analyst")

# YAHAN NAYI KEY DAALEIN
genai.configure(api_key="AIzaSyBeSaJ1Sx-5vLcq0J1AfofA2Zun9tOF_X0")
#se stable model use kar rahe hain
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

    try:
        # Simple call bina kisi extra setting ke
        response = model.generate_content(f"Answer briefly as Sameed's AI: {prompt}")
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"Error: {e}")
