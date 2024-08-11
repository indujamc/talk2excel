import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from langchain_groq.chat_models import ChatGroq
import os

os.environ['GROQ_API_KEY'] = "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"

llm = ChatGroq(model_name="mixtral-8x7b-32768", api_key=os.environ["GROQ_API_KEY"])

st.title('Talk to Excel')

uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    df = SmartDataframe(df, config={"llm": llm})
    
    user_question = st.text_input("Ask a question about the data:")
    
    if user_question:
        try:
            response = df.chat(user_question)
            # Check if the response is meaningful; if not, provide feedback
            if not response or "No code found" in response:
                st.write("Sorry, I couldn't find an answer based on the data provided. Please try another question.")
            else:
                st.write(response)
        except Exception as e:
            st.write(f"An error occurred: {e}")
