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

selected = option_menu(menu_title=None,  # required
            options=["CyberBullying Detector", "Online Harassment Detector"],  # required
            icons=["shield-fill-check", "exclamation-triangle"],  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )

header = st.container()
dataset = st.container()
features= st.container()
modelTraining = st. container()


if selected == "Cyber Bullying Detector":
    st.text(f"Cyberbullying Information") #replace with the model page

    with dataset:
        
        data, user_info = backend.final_predictions('bullying')
        st.header("Potential Bullying Report")
        st.write(data.head())
        st.header("User Report")
        st.write(user_info.head())
        
    with features:
        st.header("Features")
        st.write("Currently, CyberFence scrapes tweets from Twitter using keywords generated from a Machine Learning algorithm and obtains a list of users and their tweets for a 24 hour period that might be actively engaging in cyberbullying and harassment. We then pass this data to a NLP model that classifies the tweet. We then process this dataset to look for any repeat offenders. If flagged we would pass this information directly to law enforcement agencies to take action.")
        st.markdown("More often than not, victims of cyber crimes don’t come forward and even if they do report the harmful content, action taken is too little too late.As young students ourselves, we have seen the kind of hatred people online are capable of firsthand. Which is why we built CyberFence.")
        st.markdown("**CyberFence is designed with the intention of being a resource that can bridge the gap between law enforcement agencies and social media corporations like Twitter by using publicly available tweets to flag people who are repeat offenders.**")


if selected == "Hate Speech Detector":
    st.text(f"Hate Speech Information") #replace with the model page

    data, user_info = backend.final_predictions('hatespeech')
    st.header("Potential Hate Speech Report")
    st.write(data.head())
    st.header("User Report")
    st.write(user_info.head())




