import base64
import io
import json
from proxy import lts_proxy
from PIL import Image
import streamlit as st

DATA_FORMAT = 'image/png'

prompt = st.chat_input("Enter your prompt for image generation")

if prompt:
    proxy = lts_proxy.Proxy()
    image_base64 = proxy.get_image(prompt)
    
    if image_base64:
        image_bytes = base64.b64decode(image_base64)
        image = Image.open(io.BytesIO(image_bytes))
        st.image(image, caption=f"Generated image for prompt: {prompt}")

        st.download_button(label='Download', 
                          data=image_bytes, 
                          file_name='download.png', 
                          mime=DATA_FORMAT)
    else:
        st.error("Failed to generate image. Please try again.")
