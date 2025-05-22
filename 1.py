import streamlit as st
import openai

st.title("Whisper Audio Transcription (Web Demo)")

api_key = st.text_input("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", type="password")
audio_file = st.file_uploader("Upload audio file", type=["wav", "mp3", "m4a"])

if api_key and audio_file:
    st.audio(audio_file)
    if st.button("Transcribe"):
        with st.spinner("Transcribing..."):
            client = openai.OpenAI(api_key=api_key)
            response = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )
            st.success("Transcription:")
            st.write(response.text)
