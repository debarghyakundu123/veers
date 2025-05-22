import streamlit as st
import tempfile
import os
import whisper

st.title("Offline Audio Transcription with Whisper")
st.write("Upload an audio file (wav, mp3, m4a) and get a transcription. No API key required!")

# File uploader
uploaded_file = st.file_uploader("Choose an audio file", type=["wav", "mp3", "m4a"])

if uploaded_file is not None:
    # Save uploaded file to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=uploaded_file.name) as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    st.audio(tmp_path)

    # Whisper expects a file path. Convert audio if needed.
    audio_path = tmp_path
    if not tmp_path.lower().endswith('.wav'):
        # Convert to wav using ffmpeg
        import ffmpeg
        wav_path = tmp_path + ".wav"
        try:
            ffmpeg.input(tmp_path).output(wav_path, acodec='pcm_s16le', ac=1, ar='16000').run(overwrite_output=True, quiet=True)
            audio_path = wav_path
        except Exception as e:
            st.error(f"FFmpeg conversion failed: {e}")
            os.unlink(tmp_path)
            st.stop()

    # Load Whisper model
    st.info("Loading Whisper model (first time may take a while)...")
    model = whisper.load_model("base")  # You can use "base", "small", "medium", or "large"

    # Transcribe
    st.info("Transcribing audio...")
    result = model.transcribe(audio_path)
    st.subheader("Transcription")
    st.write(result["text"])

    # Clean up
    os.unlink(tmp_path)
    if audio_path != tmp_path:
        os.unlink(audio_path)
