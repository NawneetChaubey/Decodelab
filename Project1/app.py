#Streamlit library for UI
import streamlit as st

# Backend Logic for UI
from LogicBot import get_response

# Configuration of UI 
st.set_page_config(
    page_title="LogicBot",
    page_icon="🤖",
    layout="centered"
)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "👋 Hello! I am LogicBot. Type 'help' to see available commands."
        }
    ]

with st.sidebar:
    st.title("🤖LogicBot")
    st.markdown("### Available Commands")

    commands = [
    "hello",
    "how are you",
    "what is your name",
    "who are you",
    "what can you do",
    "what is ai",
    "what is python",
    "tell me a joke",
    "motivate me",
    "version",
    "thanks",
    "bye"
]
    
    for cmd in commands:
        st.write(f"• {cmd}")
    
    st.markdown("---")

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.caption("DecodeLabs AI Project 1")

st.title("🤖LogicBot")
st.caption("Rule-Based Chatbot")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Type your message.......")

if user_input:
    st.session_state.messages.append(
        {
            "role":"user",
            "content": user_input
        }
    )
    
    response = get_response(user_input)
    
    st.session_state.messages.append(
        {
            "role":"assistant",
            "content": response
        }
    )

    st.rerun()