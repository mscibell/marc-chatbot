import streamlit as st
import openai

# Set OpenAI API Key
openai.api_key = "your_openai_api_key"  # Replace with your actual OpenAI API key

# Title of the chatbot app
st.title("💬 Chat with My AI Assistant")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User input box
user_input = st.chat_input("Type your message here...")

if user_input:
    # Store user's message
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    # Generate AI response
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=st.session_state.messages
    )

    # Get AI response text
    reply = response['choices'][0]['message']['content']
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.chat_message("assistant
