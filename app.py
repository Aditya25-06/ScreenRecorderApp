# app.py
import streamlit as st
from main import start_recording  # adjust if your main.py has a function to start recording

st.title("Screen Recorder App")

st.write("Click the button to start recording your screen:")

if st.button("Start Recording"):
    st.write("Recording started...")
    start_recording()  # call your existing function
    st.write("Recording finished!")
