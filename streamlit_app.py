import streamlit as st
import pandas as pd


header = st.container()
dataset = st.container()
features= st.container()
modelTraining = st. container()

with header:
    st.title("insert name")
    st.text("add description")

with dataset:
    st.header("Our dataset")
    data = pd.read_csv("data/bully1.csv")
    st.write(data.head())

with features:
    st.header("Features")

with modelTraining:
    st.header("The model")

