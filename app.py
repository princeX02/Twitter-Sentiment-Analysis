import streamlit as st
import requests


# FastAPI endpoint
API_URL = "http://127.0.0.1:8000/predict"

# Streamlit app title
st.set_page_config(page_title="Twitter Sentiment Analysis", page_icon="💬", layout="centered")

st.title("💬 Twitter Sentiment Analysis")
st.write("Analyze the sentiment of any tweet using a trained ML model (FastAPI + Streamlit).")

# User input
tweet_text = st.text_area("Enter a Tweet:", placeholder="Type something like 'I love using ChatGPT!'")

if st.button("Predict Sentiment"):
    if tweet_text.strip() == "":
        st.warning("⚠️ Please enter a tweet to analyze.")
    else:
        # Send request to FastAPI
        payload = {"text": tweet_text}
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            result = response.json()
            sentiment = result["sentiment"]

            # Display result
            if "Positive" in sentiment:
                st.success(f"🌟 Sentiment: {sentiment}")
            elif "Negative" in sentiment:
                st.error(f"💢 Sentiment: {sentiment}")
            else:
                st.info(f"😐 Sentiment: {sentiment}")
        else:
            st.error("❌ API request failed. Please make sure the FastAPI server is running.")
