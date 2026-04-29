import streamlit as st
import pickle
from preprocess import preprocess_text


model  = pickle.load(open('model.pkl', 'rb'))
vectorizer  = pickle.load(open('vectorizer.pkl', 'rb'))

st.title('Movie Sentiment Classifier')

text = st.text_input("Enter any movie review:")

if st.button('Classify'):
    print("Working...")
    preprocessed_text = preprocess_text(text)
    text_vectorized = vectorizer.transform(preprocessed_text)
    result = model.predict(text_vectorized)[0]
    print(result)
    if result == 'positive':
        st.success('Positive Review')
    if result == 'negative':
        st.error('Negative Review')

#The movie was fantastic! I really enjoyed it.