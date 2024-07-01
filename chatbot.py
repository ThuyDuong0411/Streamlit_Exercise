import streamlit as st
from hugchat import hugchat
from hugchat.login import Login
# function for generating LLM respone


def generate_response(prompt_input, email, passwd):
    # hugging face login
    sign = Login(email, passwd)
    cookies = sign.login()
    # creat chatbot
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    return chatbot.chat(prompt_input)


def main():
    st.title("Simple Chatbot")
    with st.sidebar:
        hf_email = st.text_input("Email")
        hf_pass = st.text_input("Password", type='password')
        if not (hf_email and hf_pass):
            st.warning("Please enter your account!")
        else:
            st.success("Process to entering your prompt message!")
# store LLM generated respones
    if "messages" not in st.session_state.keys():
        st.session_state.messages = [
            {"role": "assistant", "content": "How  may I help you?"}]
# display chat message
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
# user provied prompt
    if prompt := st.chat_input(disabled=not (hf_email and hf_pass)):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
# Generate a new respone if last message is not from assistant
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = generate_response(prompt, hf_email, hf_pass)
                st.write(response)
        message = {"role": "assistant", "content": response}
        st.session_state.messages.append(message)


if __name__ == "__main__":
    main()
