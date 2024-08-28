import base64
import io
from proxy import lts_proxy
from PIL import Image
import streamlit as st

DATA_FORMAT = 'audio/mp3'

input = st.chat_input("Enter your text to convert to speech")

if input:
    proxy = lts_proxy.Proxy()
    audio_base64 = proxy.get_speech(input)
    
    if audio_base64:
        audio_bytes = base64.b64decode(audio_base64)
        audio_io = io.BytesIO(audio_bytes)
        st.audio(audio_io, format=DATA_FORMAT)

        st.download_button(label='Download', 
                    data=audio_bytes, 
                    file_name='download.mp3', 
                    mime=DATA_FORMAT)
    else:
        st.error("Failed to convert text to speech. Please try again.")
