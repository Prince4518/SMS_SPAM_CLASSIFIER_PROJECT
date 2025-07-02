# SMS_SPAM_CLASSIFIER_PROJECT
# SMS Spam Classifier 📱🚫

This is a simple machine learning web app that classifies SMS messages as **Spam** or **Not Spam**.

## 🔍 About the Project

This project uses **Natural Language Processing (NLP)** with a **Multinomial Naive Bayes** model trained on SMS messages. The goal is to detect spam messages.

I created this project to learn about ML, text processing, and how to build and deploy ML apps using **Streamlit**.

## 🛠 Tech Stack

- Python 🐍
- Scikit-learn 🤖
- Pandas 📊
- Streamlit 🌐

## 📂 Files in the Repository

- `app.py` → Main Streamlit app
- `vectorizer.pkl` → Fitted TF-IDF vectorizer
- `spam_classifier.pkl` → Trained ML model
- `requirements.txt` → All Python dependencies
- `spam_detector.ipynb` → Jupyter notebook for training the model

## 🚀 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py

