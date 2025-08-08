import streamlit as st
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.chat_logic import get_response

# Page configuration
st.set_page_config(
    page_title="Yabatech Chatbot",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Title and welcome message
st.title("Yabatech FAQ Chatbot")
st.markdown("Ask me anything about Yabatech. I'm here to help!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Type your question here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get bot response
    response = get_response(prompt)

    # Display bot response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add bot response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Optional: Add icons (non-functional for now)
st.sidebar.markdown("---")
st.sidebar.markdown("### Settings")

# Mic icon
st.sidebar.button("🎤 Start Voice Input")

# Globe icon
st.sidebar.button("🌐 Toggle Language")
