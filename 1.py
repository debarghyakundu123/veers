import streamlit as st
import whisper
import tempfile

# Load the Whisper model once
model = whisper.load_model("base")

st.title("Audio Transcription with Whisper")

uploaded_file = st.file_uploader("Upload an audio file (mp3, wav, etc.)", type=["mp3", "wav", "m4a"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
        temp_audio.write(uploaded_file.read())
        temp_audio_path = temp_audio.name

    st.write("Transcribing... please wait.")
    result = model.transcribe(temp_audio_path)
    st.subheader("Transcription:")
    st.write(result["text"])
