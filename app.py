# app.py
import streamlit as st
import threading
from datetime import datetime
from recorder import record_screen, capture_screen

# Streamlit app title
st.title("Screen Recorder App")
st.write("Record your screen directly from your browser!")

# Use session state to track recording
if "recording" not in st.session_state:
    st.session_state.recording = False
if "stop_flag" not in st.session_state:
    st.session_state.stop_flag = {"stop": False}

# Function to run recording in a separate thread
def run_recording(filename):
    st.session_state.stop_flag["stop"] = False
    record_screen(st.session_state.stop_flag, filename)
    st.session_state.recording = False
    st.success(f"Recording finished! Saved as {filename}")

st.write("---")

# Buttons for recording
if not st.session_state.recording:
    if st.button("▶ Start Recording"):
        # Filename with timestamp
        filename = f"Recording_{datetime.now().strftime('%Y%m%d_%H%M%S')}.avi"
        st.session_state.recording = True
        threading.Thread(target=run_recording, args=(filename,)).start()
        st.info("Recording started...")
else:
    if st.button("⏹ Stop Recording"):
        st.session_state.stop_flag["stop"] = True
        st.session_state.recording = False
        st.warning("Recording stopped!")
