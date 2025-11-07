import streamlit as st
import requests

# -------------------------------
# Set your FastAPI endpoint here
# -------------------------------
# For local testing:
# API_URL = "http://127.0.0.1:8000/predict"

# For deployed FastAPI on Render:
API_URL = "https://twitter-sentiment-analysis-3-07m6.onrender.com/predict"

# -------------------------------
# Streamlit page config
# -------------------------------
st.set_page_config(
    page_title="Twitter Sentiment Analysis",
    page_icon="💬",
    layout="centered"
)

st.title("💬 Twitter Sentiment Analysis")
st.write("Analyze the sentiment of any tweet using a trained ML model (FastAPI + Streamlit).")

# -------------------------------
# User input
# -------------------------------
tweet_text = st.text_area(
    "Enter a Tweet:",
    placeholder="Type something like 'I love using ChatGPT!'"
)

# -------------------------------
# Predict sentiment button
# -------------------------------
if st.button("Predict Sentiment"):
    if tweet_text.strip() == "":
        st.warning("⚠️ Please enter a tweet to analyze.")
    else:
        payload = {"text": tweet_text}

        try:
            response = requests.post(API_URL, json=payload, timeout=10)
            response.raise_for_status()  # Raises error for HTTP codes 4xx/5xx

            result = response.json()
            sentiment = result.get("sentiment", "Unknown")

            # Display result
            if "Positive" in sentiment:
                st.success(f"🌟 Sentiment: {sentiment}")
            elif "Negative" in sentiment:
                st.error(f"💢 Sentiment: {sentiment}")
            else:
                st.info(f"😐 Sentiment: {sentiment}")

        except requests.exceptions.RequestException as e:
            st.error(f"❌ API request failed: {e}")
