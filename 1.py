import streamlit as st
import whisper
import tempfile

st.title("Whisper Audio Transcription")

uploaded_file = st.file_uploader("Upload audio file", type=["wav", "mp3", "m4a"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    st.write("Loading Whisper model...")
    model = whisper.load_model("base")

    st.write("Transcribing audio...")
    result = model.transcribe(tmp_path)
    st.subheader("Transcription")
    st.write(result["text"])
