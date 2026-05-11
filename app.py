import streamlit as st 
from llm import create_llm

st.set_page_config(
    page_title = 'Multi-PDF Chatbot',
    page_icon = '📄',
    layout = 'wide',
    initial_sidebar_state = 'expanded'
)

st.title('📄 Conversational Multi-PDF RAG Chatbot')
st.write('Upload multiple PDF documents and ask context-aware questions about their content.')


with st.sidebar:
    st.header('Upload Documents')
    uploaded_pdfs = st.file_uploader(
        'Choose a Pdf File',
        type = ['pdf'],

    accept_multiple_files=True
    )

if 'history' not in st.session_state:
    st.session_state.history = []

if 'messages' not in st.session_state:
    st.session_state.messages = []

for messages in st.session_state.messages:
    with st.chat_message(messages['role']):
        st.markdown(messages['content'])
        

if prompt:= st.chat_input("Enter Query Here"):
    with st.chat_message('user'):
        st.markdown(prompt)
    st.session_state.messages.append({'role': 'user' , 'content': prompt})
    answer = create_llm(prompt, st.session_state.history)

    with st.chat_message('assistant'):
        st.markdown(answer)
    
    st.session_state.messages.append({'role': 'assistant', 'content': answer})
    st.session_state.history.append(f"User: {prompt}")
    st.session_state.history.append(f"Assistant: {answer}")