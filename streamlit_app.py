
    load_dotenv()
    st.set_page_config(page_title="Chat with your file")
 
        st.session_state.processComplete = None
ated...")
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
    for uploaded_file in uploaded_files:
        split_tup = os.path.splitext(uploaded_file.name)
        file_extension = split_tup[1]
      

def get_text_chunks(text):
    # spilit ito chuncks
    text_splitter = Chara






