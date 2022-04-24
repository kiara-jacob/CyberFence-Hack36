import backend
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

col1, mid, header = st.columns([1,5,20])
with col1:
    st.image('/Users/kiarajacob/GitHubHack36/cyberfence_logo.png', width=120)

with header:
    st.title("CyberFence")
st.write("With the advent of the internet and social media apps like Twitter, there has been a major uptick in crimes like Cyberbullying and Online Harassment.")
st.markdown("More often than not, victims of cyber crimes don’t come forward and even if they do report the harmful content, action taken is too little too late.As young students ourselves, we have seen the kind of hatred people online are capable of firsthand. Which is why we built CyberFence.")
st.markdown("**CyberFence is designed with the intention of being a resource that can bridge the gap between law enforcement agencies and social media corporations like Twitter by using publicly available tweets to flag people who are repeat offenders.**")

header = st.container()
dataset = st.container()
features= st.container()
modelTraining = st. container()

with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=['Cyber Bullying Detector','Harassment Detector'],
    )

if selected == "Cyber Bullying Detector":
    st.text(f"Cyberbullying Information") #replace with the model page

    with dataset:
        
        data, user_info = backend.final_predictions('bullying')
        st.header("Potential Bullying Report")
        st.write(data.head())
        st.header("User Report")
        st.write(user_info.head())

if selected == "Hate Speech Detector":
    st.text(f"Hate Speech Information") #replace with the model page

    data, user_info = backend.final_predictions('hatespeech')
    st.header("Potential Hate Speech Report")
    st.write(data.head())
    st.header("User Report")
    st.write(user_info.head())




