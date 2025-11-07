# Sentiment Analysis Web Application

[![Python](https://img.shields.io/badge/python-3.13-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.0-green)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25-orange)](https://streamlit.io/)

---

## **Project Overview**
This project is a **Sentiment Analysis Web Application** that predicts the sentiment (positive, negative, neutral) of user-input text using a **pre-trained machine learning model**.  

- **Backend**: FastAPI  
- **Frontend**: Streamlit  
- **Model**: Machine learning / NLP model trained on [mention dataset]  
- **Goal**: Provide a fast, interactive, and user-friendly platform to analyze sentiment in real-time text input.  

---

## **Features**
- Real-time sentiment prediction
- Interactive web interface via Streamlit
- REST API endpoints powered by FastAPI
- Easy-to-deploy architecture for production
- Docker-ready for containerized deployment (optional)

---

## **Tech Stack**
| Layer       | Technology      |
|------------|----------------|
| Backend    | FastAPI         |
| Frontend   | Streamlit       |
| Model      | scikit-learn / TensorFlow / PyTorch (depending on your model) |
| Data       | CSV / JSON      |
| Deployment | GitHub / Render |

---

## **Installation**

### **1. Clone the repository**
```bash
git clone https://github.com/princeX02/Twitter-Sentiment-Analysis.git
cd Twitter-Sentiment-Analysis
```

### **2. Set up a virtual environment**
```bash
python -m venv myenv
source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
```

### **3. Install dependencies**
```bash
pip install -r requirements.txt


```### **4. Run the FastAPI backend**
```bashuvicorn app.main:app --reload
``` 

### **5. Run the Streamlit frontend**
```bash
streamlit run app_streamlit.py  
```
### **6.Backend Deployment**
```bash
You can deploy the FastAPI backend on platforms like Render, Heroku, or AWS. Follow their specific deployment guides.
```

### **7. Run the application**
```bash
Open your web browser and navigate to `https://ywcwavvnafycafgzcoccuw.streamlit.app/` to access the Streamlit frontend.
```

