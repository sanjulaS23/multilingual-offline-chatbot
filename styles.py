import streamlit as st


def load_css():

    st.markdown("""
    <style>

    .stApp{
        background:#f0f2f5;
    }

    .user-bubble{
        background:#DCF8C6;
        color:black;
        padding:12px;
        border-radius:15px;
        margin-bottom:10px;
    }

    .bot-bubble{
        background:white;
        color:black;
        padding:12px;
        border-radius:15px;
        margin-bottom:10px;
    }

    </style>
    """, unsafe_allow_html=True)