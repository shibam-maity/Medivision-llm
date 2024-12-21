import os
import streamlit as st # type: ignore
import google.generativeai as genai # type: ignore
from api_key import api_key  # Import your API key

# System Prompt
system_prompt = """
You are a highly advanced medical image analysis expert with extensive knowledge in radiology, pathology, and diagnostic imaging. Your role is to assist with analyzing medical images to provide valuable insights while adhering to professional and ethical standards.

Your Responsibilities:
- Thorough Analysis: Carefully examine each image to identify abnormalities, anomalies, or signs of disease with precision and clarity.
- Findings Documentation: Provide a clear, concise report detailing observed issues, highlighting their clinical significance, and noting any areas of uncertainty.
- Actionable Recommendations: Suggest potential next steps, such as additional tests, referrals to specialists, or further diagnostic procedures based on your findings.
- Treatment Suggestions (If Applicable): Recommend possible interventions or treatments, ensuring they align with your analysis, but emphasize consulting with a medical professional.

Guidelines:
- Focus on Relevance: Respond only if the image pertains to human health or clinical diagnostics.
- Image Quality Considerations: If the image quality hinders analysis, clearly state the limitations and suggest re-evaluation with higher-quality imaging.
- Disclaimer: Conclude every analysis with the following disclaimer:
  "This analysis is for informational purposes only. Please consult a licensed medical professional before proceeding with any medical decisions."

Tone and Presentation:
- Use professional and concise language.
- Avoid technical jargon unless necessary for accuracy.
- Ensure your responses are patient-centered and clinically actionable.
"""

# Configure genai with API key
genai.configure(api_key=api_key)

# Set the page configuration
st.set_page_config(page_title="MediVision", page_icon="🔬")

# Set up the Streamlit interface
st.image("Computer-Vision-AI-new.jpg", width=700, )  # Logo image
st.title("🔬 MediVision 🧬")
st.subheader("An application that helps users analyze medical images")

# File uploader for medical image
uploaded_file = st.file_uploader("Upload the medical image for analysis", type=["png", "jpg", "jpeg"])
submit_button = st.button("Generate Analysis")

# Function to upload file to Gemini
def upload_to_gemini(path, mime_type=None):
    """Uploads the given file to Gemini."""
    file = genai.upload_file(path, mime_type=mime_type)
    return file

# Function to analyze the image using Google Generative AI
def analyze_image(file_path):
    """Analyze the uploaded image using Google Generative AI."""
    file = upload_to_gemini(file_path, mime_type="image/jpeg")
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        generation_config=generation_config,
    )
    # Include system instructions in the user's initial message
    chat_session = model.start_chat(
        history=[
            {"role": "user", "parts": [f"{system_prompt}\nAnalyze this medical image."]},
            {"role": "user", "parts": [file]},  # Correctly pass the file
        ]
    )
    response = chat_session.send_message("Please analyze the uploaded medical image.")
    return response.text

# When the user clicks the "Generate Analysis" button
if submit_button and uploaded_file is not None:
    # Save the uploaded file temporarily
    with open("temp_image.jpeg", "wb") as temp_file:
        temp_file.write(uploaded_file.getbuffer())

    try:
        # Analyze the uploaded image
        analysis_result = analyze_image("temp_image.jpeg")
        st.success("Analysis Generated Successfully!")
        st.write(analysis_result)  # Display the analysis result
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
    finally:
        # Clean up the temporary file
        if os.path.exists("temp_image.jpeg"):
            os.remove("temp_image.jpeg")
