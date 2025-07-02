import streamlit as st
import pickle

# Load the trained model and vectorizer
@st.cache_resource
def load_model_and_vectorizer():
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
    return model, vectorizer

model, vectorizer = load_model_and_vectorizer()

# Streamlit UI
st.title("Spam Message Classifier")
st.write("Enter a message to check if it's spam or not.")

user_input = st.text_area("Message", "")

if st.button("Classify"):
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        # Vectorize the input
        input_vec = vectorizer.transform([user_input])
        # Predict
        prediction = model.predict(input_vec)[0]
        # Show result
        if prediction == 1 or prediction == 'spam':
            st.error("This message is **SPAM**.")
        else:
            st.success("This message is **NOT SPAM**.")