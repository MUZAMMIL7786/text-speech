import streamlit as st
import speech_recognition as sr

def recognize_speech_from_microphone():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        st.write("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source)
        st.write("Ready to receive input. Speak now!")
        audio = recognizer.listen(source)

    st.write("Processing input...")
    try:
        transcription = recognizer.recognize_google(audio)
        return transcription
    except sr.RequestError:
        return "API unavailable"
    except sr.UnknownValueError:
        return "Unable to recognize speech"

st.title("Speech to Text Note Taking App")

st.write("Click the button below and start speaking. Your speech will be transcribed into text notes.")

if st.button("Start Recording"):
    transcription = recognize_speech_from_microphone()
    st.write("You said:")
    st.write(transcription)
    with open("notes.txt", "a") as f:
        f.write(transcription + "\n")
    st.write("Your notes have been saved.")
