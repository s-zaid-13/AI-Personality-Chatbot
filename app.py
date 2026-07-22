import streamlit as st
from prompts import PERSONALITIES
from groq_helper import generate_response

st.set_page_config(page_title="AI Personality Chatbot", page_icon="🤖", layout="wide")

# Sidebar

st.sidebar.header("⚙️ Chat Settings")

AVAILABLE_MODELS = [
    # General / Reasoning
    "llama-3.3-70b-versatile",
    "llama-3.1-8b-instant",
    "openai/gpt-oss-120b",
    "openai/gpt-oss-20b",
    # Multimodal / Vision
    "qwen/qwen3.6-27b",
    # Built-in Agent Tools
    "groq/compound",
    # Audio & Safety
    "whisper-large-v3-turbo",
    "openai/gpt-oss-safeguard-20b",
]

selected_model = st.sidebar.selectbox("Select AI Model", AVAILABLE_MODELS)

selected_personality = st.sidebar.selectbox(
    "Select Personality", list(PERSONALITIES.keys())
)

st.sidebar.markdown("---")

st.sidebar.success(f"🤖 Model\n\n{selected_model}")
st.sidebar.info(f"🎭 Personality\n\n{selected_personality}")

st.sidebar.markdown("---")

if st.sidebar.button("🗑 Clear Chat", use_container_width=True):
    st.session_state.messages = []
    st.rerun()

# Main Page
st.title("🤖 AI Personality Chatbot")
st.caption("Powered by Groq • Streamlit • Multiple AI Personalities")

st.markdown("---")

# Session Memory

if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


user_prompt = st.chat_input("Type your message...")


if user_prompt and user_prompt.strip():

    st.session_state.messages.append({"role": "user", "content": user_prompt})

    with st.chat_message("user", avatar="👤"):
        st.markdown(user_prompt)

    with st.spinner("Generating response..."):

        ai_response = generate_response(
            model_name=selected_model,
            personality_prompt=PERSONALITIES[selected_personality],
            chat_history=st.session_state.messages,
        )

    st.session_state.messages.append({"role": "assistant", "content": ai_response})

    with st.chat_message("assistant"):
        st.markdown(ai_response)


hide_streamlit_style = """
<style>
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown(hide_streamlit_style, unsafe_allow_html=True)
