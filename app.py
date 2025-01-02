import streamlit as st
import google.generativeai as genai
from PIL import Image
import os
import time
from api_key import api_key

# Configure Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-pro')

# Initialize chat
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# System prompt
system_prompt = """You are a medical imaging expert AI assistant. When analyzing images, provide:
1. Detailed description
2. Potential diagnoses
3. Key anatomical structures
4. Abnormalities
5. Image quality assessment
6. Recommendations

For general medical questions, be informative while noting you're not a replacement for professional medical advice.
Be conversational but professional in your responses."""

# Enhanced response generation
def get_gemini_response(input_text, image=None, max_retries=3):
    for attempt in range(max_retries):
        try:
            if image:
                response = model.generate_content([input_text, image])
            else:
                response = st.session_state.chat.send_message(input_text)
            return response.text
        except Exception as e:
            if "429" in str(e) and attempt < max_retries - 1:
                time.sleep(2)
                continue
            return f"Sorry, I'm currently experiencing issues. Please try again. Error: {str(e)}"

# Streamlit UI
st.title("MediVision AI Assistant")


# Chat container
chat_container = st.container()
with chat_container:
    for role, message in st.session_state.chat_history:
        with st.chat_message(role):
            if isinstance(message, tuple) and message[0] == "image":
                st.image(message[1], caption="Uploaded Medical Image")
                st.write(message[2])
            else:
                st.write(message)

# Sidebar
with st.sidebar:
    st.header("Upload Medical Image")
    uploaded_file = st.file_uploader("Choose a medical image...", type=["jpg", "jpeg", "png"])
    
    # Clear Chat button
    if st.button("Clear Chat"):
        try:
            # Clear all session state
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            
            # Reinitialize chat
            st.session_state.chat = model.start_chat(history=[])
            st.session_state.chat_history = []
            
            # Clear all caches
            st.cache_data.clear()
            st.cache_resource.clear()
            
            # Show success message
            st.success("Chat cleared! Refreshing page...")
            
            # Force a complete page reload using JavaScript
            st.markdown(
                """
                <script>
                    window.parent.location.reload();
                </script>
                """,
                unsafe_allow_html=True
            )
            
            # Backup rerun in case JavaScript doesn't work
            st.rerun()
            
        except Exception as e:
            st.error(f"Error clearing chat: {str(e)}")

# Handle image upload
if uploaded_file and "image_processed" not in st.session_state:
    try:
        image = Image.open(uploaded_file)
        with st.spinner('Analyzing image...'):
            # Add context to image analysis
            response = get_gemini_response(
                f"{system_prompt}\nPlease analyze this medical image:", 
                image
            )
        
        st.session_state.chat_history.append(("user", ("image", image, "Uploaded a medical image for analysis")))
        st.session_state.chat_history.append(("assistant", response))
        st.session_state.image_processed = True
        st.rerun()
        
    except Exception as e:
        st.error(f"❌ Error processing image: {str(e)}")

# User input
user_input = st.chat_input("Ask me anything about the image or any medical questions...")

# Handle text input
if user_input:
    # Show user message immediately
    st.chat_message("user").write(user_input)
    
    # Generate response
    with st.spinner('Thinking...'):
        response = get_gemini_response(user_input)
    
    # Show assistant response
    st.chat_message("assistant").write(response)
    
    # Update chat history
    st.session_state.chat_history.append(("user", user_input))
    st.session_state.chat_history.append(("assistant", response))

# Footer
with st.sidebar:
    st.markdown("---")
    st.markdown("*Note: This AI assistant is for informational purposes only and should not replace professional medical advice.*")