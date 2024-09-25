import streamlit as st
import random
import time
import ollama


# Streamed response emulator
def response_generator(prompt):
    response = ollama.generate(model='gemma2-2-it-h.Q8_0', prompt=prompt, stream=True)

    for chunk in response:
        if chunk["response"] == "\n":
            chunk["response"] = "\n\n"
        yield chunk["response"]


st.title("특허 명세서 생성기")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("대략적인 발명의 방법을 알려주세요"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator(prompt))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})