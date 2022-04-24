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
    st.text(f"You have selected bullying model") #replace with the model page

    with dataset:
        st.header("Our dataset")
        data = pd.read_csv("data/data_final.csv")
        st.write(data.head())

    with features:
        st.header("Features")

    with modelTraining:
        st.header("The model")

if selected == "Harassment Detector":
    st.text(f"You have selected harassment model") #replace with the model page

    with dataset:
        st.header("Our dataset")
        data = pd.read_csv("data/data_final_harassment.csv")
        st.write(data.head())

    with features:
        st.header("Features")

    with modelTraining:
        st.header("The model")




