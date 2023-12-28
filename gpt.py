import streamlit as st
import os
from PyPDF2 import PdfReader
import doc
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalCha
# "with" notation
def main():
    load_dotenv()
    st.set_page_config(page_ti
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    if "processComplete" not in st.session_state:
        st.session_state.processComplete = None

    with st.sidebar:
        uploaded_files =  st.file_uploader("Upload your file",type=['pdf'],accept_multiple_files=True)
        openai_api_key = hf_api_key
        # openai_api_key = st.text_input("OpenAI API Key", key=openapi_key , type="password")
        process = st.button("Process")
    if process:
        if not openai_api_key:
            st.info("Please add your OpenAI API key to continue.")
            st.stop()
        files_text = get_files_text(uploaded_files)
        st.write("File loaded...")
        # get text chunks
        text_chunks = get_text_chunks(files_text)
        st.write("file chunks created...")
        # create vetore stores
        vectorstore = get_vectorstore(text_chunks)
        st.write("Vectore Store Created...")
         # create conversation chain
        st.session_state.conversation = get_conversation_chain(vectorstore) #for openAI

        st.session_state.processComplete = True

    if  st.session_state.processComplete == True:
        user_question = st.chat_input("Ask Question about your files.")
        if user_question:
            handel_userinput(user_question)


# Function to get the input file and read the text from it.
def get_files_text(uploaded_files):
    text = ""

            text += get_docx_text(uploaded_file)
        else:
            text += get_csv_text(uploadeara.text)
    text = ' '.join(allText)
    return text

def get_csv_text(file):
    return "a"

def get_text_chunks(text):
    # spilit ito chuncks
    text_splitter = CharacterText
    )
    chunks = text_splitter.split_text(text)
    return chunks




def get_vectorstore(text_chunks):
    
    # Load Hugging Face embeddings
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    # Create FAI






