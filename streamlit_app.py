import streamlit as st
import google.generativeai as gen_ai

# Configure Streamlit page settings
st.set_page_config(
    page_title = "Chat with Gemini-Pro!",
    page_icon = ":brain:",  # Favicon emoji
    layout = "centered",  # Page layout option
)

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key = "AIzaSyC4bk1DySjdbt37IZ0sL2LlcLzjipz4hXA")
model = gen_ai.GenerativeModel('gemini-2.5-flash')

# Function to translate roles between Gemini-Pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

# Initialize chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])
    start_message = """
        You are a mental health conditioning coach. Talk to me without revealing that you are an AI.
        Keep you responses not more than 25 words.
    """ 
    
    gemini_response = st.session_state.chat_session.send_message(start_message)

# Display the chatbot's title on the page
st.title("🤖 You are Alright")

# Display the chat history
for idx, message in enumerate(st.session_state.chat_session.history):
    if idx > 0:
        with st.chat_message(translate_role_for_streamlit(message.role)):
            st.markdown(message.parts[0].text)

# Input field for user's message
user_prompt = st.chat_input("Type Here...")
if user_prompt:
    # Add user's message to chat and display it
    st.chat_message("user").markdown(user_prompt)

    # Send user's message to Gemini-Pro and get the response
    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    # Display Gemini-Pro's response
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)
