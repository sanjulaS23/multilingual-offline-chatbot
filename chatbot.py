import streamlit as st
import ollama


def generate_response():

    if st.session_state.messages[-1]["role"] != "user":
        return

    with st.spinner("Thinking..."):

        try:

            response = ollama.chat(

                model="gemma3:12b",

                messages=st.session_state.messages,

                keep_alive=-1,

                options={
                    "temperature": 0.2,
                    "num_ctx": 4096,
                    "num_predict": 256
                }

            )

            answer = response["message"]["content"]

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

            st.rerun()

        except Exception:

            st.error(
                "❌ Could not connect to Ollama. Please ensure the Ollama server is running."
            )