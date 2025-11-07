import os
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import uvicorn

# Load model and vectorizer
model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Initialize app
app = FastAPI(title="Twitter Sentiment Analysis API", version="1.0")

# Input schema
class TweetInput(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Welcome to the Twitter Sentiment Analysis API 🚀"}

@app.post("/predict")
def predict_sentiment(data: TweetInput):
    # Vectorize input text
    vectorized_text = vectorizer.transform([data.text])
    
    # Predict
    prediction = model.predict(vectorized_text)[0]
    
    sentiment = "Positive 😊" if prediction == 1 else "Negative 😠"
    return {"tweet": data.text, "sentiment": sentiment}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)