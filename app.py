import streamlit as st
import google.generativeai as genai
import os

# ----------------------------
# Setup Gemini API
# ----------------------------
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # or directly set your key here

genai.configure(api_key='AIzaSyBp88KTkypC86X73wLffxwB9kZWSqLIrYU')

# Load Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# ----------------------------
# Streamlit UI
# ----------------------------
st.set_page_config(page_title="Python Code Analyzer", layout="wide")

st.title("🐍 Python Code Analyzer & Loop Tracer by Raiden ")
st.write("Paste your Python code below to get **documentation**, **step-by-step explanation**, and **loop trace**.")

# Text area for code input
user_code = st.text_area("✏️ Paste your Python code here:", height=300)

if st.button("Analyze Code"):
    if not user_code.strip():
        st.error("Please paste some Python code before analyzing.")
    else:
        with st.spinner("Analyzing your code by raiden... ⏳"):
            prompt = f"""
            You are an advanced Python code documentation assistant.
            Given this Python code, do the following:
            1. Write detailed documentation for the code in a professional style.
            2. Explain the code step-by-step in plain English.
            3. Trace every loop in the code, showing iteration-wise flow and variables' values at each step.
            Code:
            ```
            {user_code}
            ```
            Output in **Markdown** format with clear headings.
            """

            try:
                response = model.generate_content(prompt)
                explanation = response.text

                # Display results
                st.subheader("📜 Documentation & Explanation")
                st.markdown(explanation)

            except Exception as e:
                st.error(f"Error: {e}")

