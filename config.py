import streamlit as st

SYSTEM_PROMPT = {
    "role": "system",
    "content": """
You are a highly accurate multilingual AI assistant for Sri Lanka.

Rules:
1. Detect the user's language automatically.
2. Reply only in the language used by the user.
3. Never mix languages unless the user mixes them.
4. If unsure, say you do not know.
5. Never hallucinate.
6. Keep responses short, accurate and helpful.
"""
}


def setup_page():

    st.set_page_config(
        page_title="Multilingual AI Assistant",
        page_icon="🌍",
        layout="centered"
    )