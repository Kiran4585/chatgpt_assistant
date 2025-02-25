import os
import streamlit as st
import webbrowser
import google.generativeai as genai

# Load Google Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # Set this in environment variables
if not GEMINI_API_KEY:
    st.error("❌ API key missing. Set GEMINI_API_KEY as an environment variable.")
else:
    genai.configure(api_key=GEMINI_API_KEY)

# Function to get AI response
def Reply(question):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(question)
    return response.text if response else "No response from Gemini AI."

# Streamlit Web App
st.title("💬 Smart AI Assistant")

query = st.text_input("Ask me anything:", "")
if st.button("Submit"):
    if query:
        st.write("🤖 Processing...")
        response = Reply(query)
        st.write(f"💬 Response: {response}")

        # Handle web commands
        if "open youtube" in query.lower():
            webbrowser.open("https://www.youtube.com")
        elif "open google" in query.lower():
            webbrowser.open("https://www.google.com")
        elif "bye" in query.lower():
            st.write("👋 Goodbye!")
