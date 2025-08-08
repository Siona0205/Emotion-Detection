import streamlit as st
import requests

st.set_page_config(page_title="AI-Powered Mental Health Assistant")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("💬 AI-Powered Mental Health Assistant")
st.write("Hello! Tell me how you're feeling today...")

# Display the chat history
for msg in st.session_state.messages:
    st.write(f"**You:** {msg['user']}")
    st.write(f"**Bot:** {msg['bot']}")

# Input form
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("You:", key="input", placeholder="Type your message...")
    submitted = st.form_submit_button("Send")

if submitted and user_input:
    try:
        response = requests.post("http://127.0.0.1:5000/analyze", json={"text": user_input})

        if response.status_code == 200:
            result = response.json()
            emotion = result.get("emotion", "Not Detected")

            st.session_state.messages.append({
                "user": user_input,
                "bot": f"Detected Emotion: {emotion}"
            })

        else:
            st.session_state.messages.append({
                "user": user_input,
                "bot": "Something went wrong. Please try again."
            })

        st.rerun()

    except requests.exceptions.JSONDecodeError:
        st.error("Invalid response from backend (not JSON).")
    except requests.exceptions.RequestException as e:
        st.error(f"Connection error: {e}")
