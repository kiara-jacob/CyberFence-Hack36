import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu


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
    with header:
        st.title("CyberFence")
        st.text("add description of bullying model")

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
    with header:
        st.title("CyberFence")
        st.text("add description of harassment model")

    with dataset:
        st.header("Our dataset")
        data = pd.read_csv("data/data_final_harassment.csv")
        st.write(data.head())

    with features:
        st.header("Features")

    with modelTraining:
        st.header("The model")




