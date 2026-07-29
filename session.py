import streamlit as st
from config import SYSTEM_PROMPT

WELCOME_MESSAGE = {
    "role": "assistant",
    "content": """
👋 Welcome to the Multilingual Offline AI Assistant!

I can answer your questions in **English, Sinhala, or Tamil**.

How can I help you today?
"""
}


def initialize_session():

    if "messages" not in st.session_state:
        st.session_state.messages = [
            SYSTEM_PROMPT,
            WELCOME_MESSAGE
        ]