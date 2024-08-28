import base64
import io
import streamlit as st
from PIL import Image
from proxy import lts_proxy

# Functions
def generate_image():
    proxy = lts_proxy.Proxy()
    st.session_state.prompt = st.session_state.input
    image_base64 = proxy.get_image(st.session_state.prompt)
    if image_base64:
        image_bytes = base64.b64decode(image_base64)
        st.session_state.image_back = Image.open(io.BytesIO(image_bytes))
    else:
        st.error("Failed to generate image. Please try again.")

def blend_images(alpha=0.4, width=2100, height=1400):
    front = st.session_state.image_front.resize((width, height))
    back = st.session_state.image_back.resize((width, height))
    st.session_state.postcard = Image.blend(front, back, alpha)

# Initialize variables in session state
if 'image_back' not in st.session_state:
    st.session_state.image_back = None
if 'image_front' not in st.session_state:
    st.session_state.image_front = None
if 'postcard' not in st.session_state:
    st.session_state.postcard = None
if 'prompt' not in st.session_state:
    st.session_state.prompt = None

# Streamlit layout
st.title("Postcard Generator")

con_1 = st.container()
con_2 = st.container()
con_3 = st.container()

with con_1:
    st.chat_input(placeholder="Enter your prompt for a generated background image", 
                  on_submit=generate_image, 
                  key='input')
    if st.session_state.image_back:
        st.image(image=st.session_state.image_back, 
                 caption=f"Generated background image for your postcard. Prompt: {st.session_state.prompt}")

with con_2:
    st.session_state.image_front = st.file_uploader(label="Upload an image of yourself", 
                                                    type=["jpg", "jpeg", "png"])
    if st.session_state.image_front:
        st.image(image=st.session_state.image_front, 
                 caption='Image of yourself for the postcard.')

with con_3:
    if st.session_state.image_front and st.session_state.image_back:
        st.session_state.image_front = Image.open(st.session_state.image_front)
        st.button(label='Create postcard', 
                  on_click=blend_images)
        if st.session_state.postcard:
            st.image(image=st.session_state.postcard, 
                    caption="Your Postcard")
            # Encode image in JPEG format
            postcard_byte_arr = io.BytesIO()
            st.session_state.postcard.save(postcard_byte_arr, format='JPEG')
            postcard_byte_arr = postcard_byte_arr.getvalue()

            st.download_button(label="Download postcard", 
                               data=postcard_byte_arr, 
                               file_name="postcard.jpg", 
                               mime="image/jpeg")

        # Additional options: Add function to send postcard via email or print it
