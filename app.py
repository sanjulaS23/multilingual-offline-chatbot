import streamlit as st

from config import setup_page
from styles import load_css
from session import initialize_session
from sidebar import sidebar
from chat import show_title, display_chat, user_input
from chatbot import generate_response

setup_page()
load_css()
initialize_session()

sidebar()
show_title()
display_chat()
user_input()
generate_response()