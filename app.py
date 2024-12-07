
import streamlit as st
import openai

# Configure OpenAI API Key
openai.api_key = "your_openai_api_key"

def analyze_code(code):
    """Analyzes the submitted code and returns feedback and fixed code."""
    prompt = f"""
    You are a Python code reviewer. Review the following code and:
    1. Identify bugs, errors, and areas for improvement.
    2. Suggest fixes or improvements.
    3. Provide the corrected version of the code.
    
    Code:
    {code}
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a code analysis assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5
        )
        review_text = response["choices"][0]["message"]["content"]
        feedback, fixed_code = review_text.split("Corrected Code:", 1)
        return feedback.strip(), fixed_code.strip()
    except Exception as e:
        return f"Error during analysis: {str(e)}", ""

# Streamlit App UI
st.set_page_config(page_title="GenAI App - AI Code Reviewer", layout="centered")
st.title("GenAI App - AI Code Reviewer")
st.subheader("Submit your Python code for analysis and receive AI-powered feedback.")

code_input = st.text_area("Paste your Python code here:", height=300)

if st.button("Review Code"):
    if code_input.strip():
        with st.spinner("Analyzing your code..."):
            feedback, fixed_code = analyze_code(code_input)
        st.subheader("Feedback")
        st.write(feedback)
        st.subheader("Fixed Code")
        st.code(fixed_code, language="python")
        if fixed_code:
            st.download_button("Download Fixed Code", fixed_code, file_name="fixed_code.py")
    else:
        st.error("Please input Python code to analyze.")
