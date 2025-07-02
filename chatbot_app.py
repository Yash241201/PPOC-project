# chatbot_app.py

import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

# Load a pretrained binary classification model (temporary for demo)
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
model.eval()

def classify_news(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    probs = F.softmax(outputs.logits, dim=1)
    pred = torch.argmax(probs, dim=1).item()
    confidence = probs[0][pred].item()
    label = "true" if pred == 1 else "fake"
    return f"This news is likely **{label}** with a confidence of {confidence * 100:.2f}%"

# Streamlit interface
st.set_page_config(page_title="Fake News Detector", layout="centered")
st.title("📰 Fake News Detector Chatbot")
st.write("Enter a news article or snippet below, and I'll predict if it's **true** or **fake**.")

user_input = st.text_area("Enter your news text here:")

if st.button("Check News"):
    if user_input.strip():
        result = classify_news(user_input)
        st.markdown(result)
    else:
        st.warning("Please enter some text.")

