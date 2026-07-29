import streamlit as st


def show_title():

   st.markdown("""
   <div style="text-align:center;padding:10px 0 30px 0;">

   <h1 style="
   font-size:42px;
   font-weight:700;
   color:#1E293B;
   margin-bottom:10px;
   ">

  🌍 Multilingual Offline Chatbot
 
  </h1>

  <p style="
  font-size:18px;
  color:#64748B;
  ">

  Powered by <b>Ollama</b> + <b>Gemma 3:12B</b>

  </p>

  </div>
  """, unsafe_allow_html=True)

st.markdown(
        "<p style='text-align:center;'>Powered by Ollama + Gemma 3:12B</p>",
        unsafe_allow_html=True
    )


def display_chat():

    for message in st.session_state.messages:

        if message["role"] == "user":

            st.markdown(
                f"<div class='user-bubble'>{message['content']}</div>",
                unsafe_allow_html=True
            )

        elif message["role"] == "assistant":

            st.markdown(
                f"<div class='bot-bubble'>{message['content']}</div>",
                unsafe_allow_html=True
            )


def user_input():

    prompt = st.chat_input("Type your message...")

    if prompt:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        st.rerun()