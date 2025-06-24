import streamlit as st
import numpy as np

def predict_message(message, model, vectorizer):
    # Define label mapping
    label_mapping = {
        0: "Not Spam", 
        1: "Spam"       
    }
    
    # Preprocess the message
    message_transformed = vectorizer.transform([message])
    
    # Predict the class and probabilities
    predicted_class = model.predict(message_transformed)[0]
    predicted_probabilities = model.predict_proba(message_transformed)[0]
    
    # Map the predicted class to its label
    predicted_label = label_mapping[predicted_class]
    
    return predicted_label, predicted_probabilities

# Streamlit app
st.title("Message Spam Detector")

# Input section
st.write("Enter a message below to check if it is 'Spam' or 'Not Spam'.")
message = st.text_area("Message", "")

# Prediction section
if st.button("Predict"):
    if message.strip():
        # Load your pre-trained model and vectorizer here
        # Example placeholders for model and vectorizer
        from sklearn.feature_extraction.text import CountVectorizer
        from sklearn.naive_bayes import MultinomialNB

        # Dummy model and vectorizer for illustration purposes
        vectorizer = CountVectorizer()
        model = MultinomialNB()

        # You must fit the vectorizer and model on your dataset before using
        # For demo purposes, we mock the transformation
        vectorizer.fit(["Hi there", "Free money", "Important meeting"])
        model.fit(vectorizer.transform(["Hi there", "Free money", "Important meeting"]), [0, 1, 0])
        
        predicted_label, predicted_probabilities = predict_message(message, model, vectorizer)
        
        st.subheader("Prediction:")
        st.write(f"*Predicted Class:* {predicted_label}")
        
        st.subheader("Prediction Probabilities:")
        st.write(f"*Not Spam:* {predicted_probabilities[0]:.2f}")
        st.write(f"*Spam:* {predicted_probabilities[1]:.2f}")
    else:
        st.error("Please enter a valid message.")