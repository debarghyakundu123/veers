import streamlit as st
import whisper
import tempfile
import os

st.title("Whisper Audio Transcription")

# Upload audio file
uploaded_file = st.file_uploader("Upload an audio file (wav, mp3, m4a)", type=["wav", "mp3", "m4a"])

if uploaded_file is not None:
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        temp_path = tmp_file.name

    st.write("Loading Whisper model (this might take a while)...")
    model = whisper.load_model("base")

    st.write("Transcribing audio... please wait.")
    result = model.transcribe(temp_path)

    # Show transcription
    st.subheader("Transcription")
    st.write(result["text"])

    # Cleanup temp file
    os.remove(temp_path)
