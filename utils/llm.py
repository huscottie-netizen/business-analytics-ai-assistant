import streamlit as st
import google.generativeai as genai

genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def ask_llm(question, context):
    prompt = f"""
You are an expert business analyst.

Answer the user's business question using the provided business context.

Business Context:
{context}

Question:
{question}

Provide:
1. Key findings
2. Possible causes
3. Recommendations

Keep the answer concise and business-oriented.
"""

    response = model.generate_content(
        prompt,
        generation_config={
            "temperature": 0.3,
        },
    )

    return response.text
