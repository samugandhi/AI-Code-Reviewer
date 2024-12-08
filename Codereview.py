import streamlit as st
import google.generativeai as genai

# Load and configure API key
def load_api_key(filepath):
    try:
        with open(filepath) as file:
            return file.read().strip()
    except FileNotFoundError:
        st.error("API key file not found. Please verify the file path.")
        st.stop()

# API key path
api_key_path = "Your API file Path here"
api_key = load_api_key(api_key_path)
genai.configure(api_key=api_key)

# Streamlit app configuration
st.set_page_config(
    page_title="AI Code Advisor",
    page_icon="💡",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Custom CSS styling
st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(to bottom, #e3f2fd, #ffffff);  /* Light blue gradient */
            color: #2c3e50;  /* Dark text for contrast */
            font-family: 'Arial', sans-serif;
        }
        .header-title {
            font-size: 2.8em;
            font-weight: 700;
            color: #1a73e8; /* Google blue */
            text-align: center;
            margin-bottom: 20px;
        }
        .description {
            font-size: 1.1em;
            color: #5f6368;
            text-align: center;
            margin-bottom: 30px;
        }
        textarea {
            background: #ffffff; 
            color: #333333;  
            border: 2px solid #ddd;
            border-radius: 6px;
            font-size: 1em;
        }
        button[kind="primary"] {
            background-color: #1a73e8; /* Bright blue for buttons */
            color: white;
            border-radius: 6px;
            font-size: 1.1em;
        }
        .subheader {
            font-size: 1.7em;
            font-weight: 600;
            color: #1a73e8; 
            margin-top: 20px;
            margin-bottom: 10px;
        }
        .report-title {
            font-size: 1.3em;
            font-weight: 600;
            color: #333333; 
            margin-bottom: 10px;
        }
        .footer {
            text-align: center;
            margin-top: 50px;
            color: #7c828a; 
            font-size: 0.9em;
        }
        .sidebar .sidebar-content {
            background-color: #1a73e8; 
            color: white;
            padding: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar configuration
st.sidebar.title("AI Code Advisor Tools")
st.sidebar.markdown(
    """
    - **🔍 Error Detection**: Pinpoint issues in your Python code.
    - **📈 Optimization Tips**: Get suggestions for improving performance.
    - **💡 Best Practices**: Receive actionable insights for writing better code.
    """,
    unsafe_allow_html=True,
)

# Main header
st.markdown('<div class="header-title">AI Code Advisor 💡</div>', unsafe_allow_html=True)
st.markdown('<div class="description">Analyze your Python code in seconds. Get error reports, performance tips, and best practices for clean, efficient coding.</div>', unsafe_allow_html=True)

# Input area for user code
code_input = st.text_area("✏️ Paste your Python code here:")

# Code review button
if st.button("Run Analysis"):
    if code_input.strip():
        with st.spinner("Processing your code..."):
            try:
                model = genai.GenerativeModel("models/gemini-1.5-flash")
                session = model.start_chat(history=[])
                feedback = session.send_message(f"Analyze this Python code:\n{code_input}")
                
                # Display results
                st.markdown('<div class="subheader">Analysis Results</div>', unsafe_allow_html=True)
                st.markdown('<div class="report-title">Insights:</div>', unsafe_allow_html=True)
                st.write(feedback.text)  # Adjust for response format if necessary
            except Exception as error:
                st.error(f"An error occurred: {error}")
    else:
        st.error("⚠️ Please paste some Python code to analyze.")

# Footer
st.markdown('<div class="footer">Crafted with ❤️ by Samrudhhi | Powered by Generative AI</div>', unsafe_allow_html=True)
