from groq import Groq
import streamlit as st


def create_groq_client():
    """
    Creates and returns a Groq client
    """

    return Groq(api_key=st.secrets["GROQ_API_KEY"])


def generate_response(model_name, personality_prompt, chat_history):
    """
    Sends messages to Groq and returns AI response
    """

    try:
        client = create_groq_client()

        messages = [{"role": "system", "content": personality_prompt}]

        messages.extend(chat_history)

        response = client.chat.completions.create(
            model=model_name, messages=messages, temperature=0.7, max_tokens=1024
        )

        return response.choices[0].message.content

    except Exception as error:
        return (
            "Unable to generate a response at the moment. "
            "Please verify your API key or internet connection and try again."
        )
