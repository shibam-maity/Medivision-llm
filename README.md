<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MediVision AI Assistant</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f4;
        }


</head>

<body>

    <div class="content-container">
        <h1>MediVision AI Assistant</h1>

        <p><strong>MediVision</strong> is an AI-powered medical imaging assistant built using <strong>Streamlit</strong> and <strong>Google Gemini API</strong>. The application allows users to upload medical images (e.g., X-rays, MRI scans) and get detailed analysis, including possible diagnoses, anatomical structures, abnormalities, image quality assessment, and recommendations. It also includes a chatbot functionality to answer general medical queries.</p>

        <h2>Features</h2>
        <ul>
            <li><strong>Medical Image Analysis</strong>: Upload a medical image, and the AI will analyze it, providing insights into anatomical structures, potential diagnoses, abnormalities, and more.</li>
            <li><strong>Conversational Chat</strong>: Ask questions related to the image or general medical topics. The AI provides conversational responses while emphasizing that it's not a substitute for professional medical advice.</li>
            <li><strong>Clear Chat Functionality</strong>: Reset the conversation and start a new analysis or ask new questions.</li>
            <li><strong>User-Friendly Interface</strong>: Built with Streamlit, allowing for smooth and interactive use.</li>
        </ul>

        <h2>Screenshots</h2>

        <h3>1. Main UI with Chat and Image Upload:</h3>
        <img src="images/ui_screenshot.png" alt="Main UI Screenshot" class="screenshot">

        <h3>2. AI Analysis of the Medical Image:</h3>
        <img src="images/ai_analysis_screenshot.png" alt="AI Analysis Screenshot" class="screenshot">

        <h3>3. System Architecture Diagram:</h3>
        <img src="images/system_architecture.png" alt="System Architecture Diagram" class="screenshot">

        <h2>System Requirements</h2>
        <ul>
            <li>Python 3.7 or higher</li>
            <li>Streamlit</li>
            <li>Google Gemini API (requires API key)</li>
            <li>PIL (Python Imaging Library) for image processing</li>
        </ul>

        <h2>Installation</h2>
        <div class="install-steps">
            <ol>
                <li><strong>Clone the repository:</strong>
                    <pre>git clone https://github.com/yourusername/Medivision-llm.git
cd Medivision-llm</pre>
                </li>
                <li><strong>Set up a virtual environment (optional but recommended):</strong>
                    <pre>python -m venv venv</pre>
                </li>
                <li><strong>Activate the virtual environment:</strong>
                    <ul>
                        <li><strong>Windows (PowerShell):</strong> <pre>.\venv\Scripts\Activate</pre></li>
                        <li><strong>macOS/Linux:</strong> <pre>source venv/bin/activate</pre></li>
                    </ul>
                </li>
                <li><strong>Install required dependencies:</strong>
                    <pre>pip install -r requirements.txt</pre>
                </li>
                <li><strong>Obtain Google Gemini API Key:</strong>
                    <ul>
                        <li>Go to the <a href="https://console.cloud.google.com/" target="_blank">Google Cloud Console</a>.</li>
                        <li>Set up a new project and enable the <strong>Google Gemini API</strong>.</li>
                        <li>Obtain the API key and save it in a file named <code>api_key.py</code> in the project directory.</li>
                    </ul>
                    <pre># api_key.py
api_key = "your_api_key_here"</pre>
                </li>
                <li><strong>Run the application:</strong>
                    <pre>streamlit run app.py</pre>
                </li>
            </ol>
        </div>

        <h2>Usage</h2>
        <ol>
            <li><strong>Upload a Medical Image</strong>: Use the file uploader in the sidebar to upload an image (e.g., JPG, JPEG, PNG).</li>
            <li><strong>Ask Questions</strong>: Type your questions in the chat input box to ask the assistant about the image or any other medical topic.</li>
            <li><strong>Analyze Results</strong>: After uploading an image, the AI will provide a detailed analysis, including possible diagnoses and recommendations.</li>
            <li><strong>Clear Chat</strong>: Click the "Clear Chat" button in the sidebar to reset the chat and start over.</li>
        </ol>

        <h2>Chatbot System Prompt</h2>
        <p>The system is configured with a special prompt that helps the AI assistant provide accurate medical insights:</p>
        <pre>
You are a medical imaging expert AI assistant. When analyzing images, provide:
1. Detailed description
2. Potential diagnoses
3. Key anatomical structures
4. Abnormalities
5. Image quality assessment
6. Recommendations

For general medical questions, be informative while noting you're not a replacement for professional medical advice.
Be conversational but professional in your responses.
        </pre>

        <h2>Example Workflow</h2>
        <ul>
            <li><strong>Upload an Image</strong>: A user uploads an image, such as an X-ray or MRI scan.</li>
            <li><strong>Analysis</strong>: The AI analyzes the image and provides a detailed response.</li>
            <li><strong>Conversational Chat</strong>: The user can ask questions about the image or general medical inquiries.</li>
            <li><strong>Response</strong>: The AI responds, helping the user understand the image's findings.</li>
        </ul>

        <h2>Contributing</h2>
        <p>We welcome contributions! Feel free to fork the repository, submit issues, or create pull requests. Make sure to follow these steps:</p>
        <ol>
            <li>Fork the repo.</li>
            <li>Create a new branch for your changes.</li>
            <li>Submit a pull request with a description of your changes.</li>
        </ol>

        <h2>Disclaimer</h2>
        <p class="note">
            This AI assistant is for informational purposes only and should not replace professional medical advice. Always consult a healthcare professional for diagnosis and treatment.
        </p>

        <div class="footer">
            <p>License: MIT License - See the <a href="LICENSE">LICENSE</a> file for details.</p>
        </div>
    </div>

</body>

</html>
