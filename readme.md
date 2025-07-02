# 📩 Spam Message Classifier

This is a simple web application built with [Streamlit](https://streamlit.io/) that classifies user-entered text messages as **Spam** or **Not Spam** using a pre-trained machine learning model.

## 🚀 Features

- Takes a message input from the user.
- Uses a trained model and vectorizer to classify messages.
- Displays clear feedback (SPAM / NOT SPAM) using Streamlit UI components.

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Prince4518/SMS_SPAM_CLASSIFIER_PROJECT
cd SMS_SPAM_CLASSIFIER_PROJECT
```

### 2. Install dependencies
Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate    # On Windows use: venv\Scripts\activate
```
Then install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Add your model files
Place your trained model and vectorizer files in the project directory:

- model.pkl
- vectorizer.pkl

Make sure these files match the structure used during training.

### 4. Run the Streamlit app

```bash
streamlit run app.py
```

## File Structure

```bash
.
├── app.py             # Streamlit application
├── model.pkl          # Trained ML model (add this)
├── vectorizer.pkl     # Fitted vectorizer (add this)
├── requirements.txt   # Dependencies
└── README.md          # Project documentation
```

## 🤖 Model Details
The classifier is trained using scikit-learn.

Any text-based classification model can be used as long as it fits the vectorizer → model → prediction pipeline.

📬 Contact
For questions or suggestions, feel free to reach out to [pp5216310@gmail.com].
