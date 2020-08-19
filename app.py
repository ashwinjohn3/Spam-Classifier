import streamlit as st
import pandas as pd
import numpy as np
import nltk.corpus
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
import joblib
nltk.download('stopwords')
st.title('Email Spam Classifier')
punctuation = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
@st.cache
def remove_punct_stopwords(message):
    form_str = [char for char in message if char not in punctuation]
    form_str_join = ''.join(form_str)
    # including subject also in the stopwords list
    words_stop = nltk.corpus.stopwords.words('english')
    words_stop.append('subject')
    form_str_stop = [word for word in form_str_join.split() if word.lower() not in words_stop]
    return form_str_stop
spam_model = joblib.load('M_NB_spam_model.joblib')
vectorizer = joblib.load('CountVectorizer.joblib')
inp_text = st.text_area('Paste the email to determine whether it is Spam or Ham',height=122)
vectorised_text = vectorizer.transform([inp_text])
prediction = spam_model.predict(vectorised_text)
if prediction == 0:
    pred = 'Ham'
else:
    pred = 'Spam'


st.write(pred)