import streamlit as st
from config import SYSTEM_PROMPT


def sidebar():

    with st.sidebar:

        st.markdown("""

        <div style="
            text-align:center;
            padding:20px;
            background:linear-gradient(135deg,#2563EB,#3B82F6);
            border-radius:18px;
            margin-bottom:25px;
        ">

        <h2 style="color:white;margin-bottom:5px;">
        🌍 AI Assistant
        </h2>

        <p style="color:#E5E7EB;margin:0;">
        Offline • Private • Secure
        </p>

        </div>

        """, unsafe_allow_html=True)

        st.success("🟢 Ollama Connected")

        st.markdown("### 💬 Chat Controls")

        if st.button(
            "🗑 Clear Chat",
            use_container_width=True
        ):

            st.session_state.messages = [SYSTEM_PROMPT]
            st.rerun()

        st.divider()

        st.markdown("### 🤖 Model")

        st.info(
            """
**Model:** Gemma 3:12B

**Runtime:** Ollama

**Mode:** Offline

**Language:** Auto Detect
"""
        )

        st.divider()

        st.caption(
            "Made with ❤️ using Streamlit and Ollama."
        )