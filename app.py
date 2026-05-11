import streamlit as st 

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