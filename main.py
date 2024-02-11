

# Run server - uvicorn main:app --host 0.0.0.0 --port 80  
#from typing import Annotated
#from fastapi import FastAPI, File, UploadFile
#from fastapi import Form
#from diffusers import StableDiffusionInstructPix2PixPipeline

#app = FastAPI()

# pipe = StableDiffusionInstructPix2PixPipeline.from_pretrained(
#     "timbrooks/instruct-pix2pix", torch_dtype=torch.float32
# )

#def check_file_type(file: UploadFile):
    #if file.content_type not in ["image/png", "image/jpg"]:
        #raise ValueError("File must be of type png or jpg")
    #return file

#@app.post("/uploadfile/")
#async def create_upload_file(your_image: UploadFile, what_do_you_want_to_look_like: str = Form(...)):
    ##### code here to call function of gen AI ####

    #return {"filename": "Hi I got the file"}

#import
from PIL import Image
import requests
import json #lottie
import streamlit as st
from streamlit_lottie import st_lottie


#function for animation
def load_lottieur1(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json

#variables for animation and for images
lottie_coding = "https://lottie.host/36c04282-cea8-4f21-b5d4-95cac05969ba/Mp56xXNS5Q.json"
img_contact_form = Image.open("images/face_alt_before.png")
img_lottie_animation = Image.open("images/face_alt_after.png")


st.set_page_config(page_title="Face Merger Machine Technology", layout="wide")

st.title("Face Merger Machine - F.M.M.")


# header section
with st.container():
    st.subheader("Welcome to this new and cutting edge technology! 馃憢") 
    st.title("A technology that will allow you to alter your appearance in just one click of a button")
    st.write("This is better than any other facial merger website in its ease of use")

# what does F.M.M. do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What does FMM do?")
        st.write("##")
        st.write(
            """
            FMM allows you to create an image with any filter of your choice. Here are the steps to creating your image:
            1. Upload your "before" picture.
            2. Enter a keyword of what you would like your picture to look like (keywords can be: American, Jennifer Lawrence, happy...)
            3. Hit the button "execute" and wait for your new and improved image to appear.
            """
        )
with right_column:
    st_lottie(lottie_coding, height=300, key="coding")

# projects
with st.container():
    st.write("---")
    st.header ("Model")
    st.write ("##")
    image_column, text_column = st.columns ((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("The before picture")
        st.write(
            """
            This is the original picture of Jennifer Lawrence
            """
            )
        #st.markdown("link to video 6:44")

with st.container():
    image_column, text_column = st.columns ((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("The after picture")
        st.write(
            '''
            This is the picture that the AI generated to make her look "Chinese"
            '''
            )
        #st.markdown("link to video 7:52")

with st.container():
    st.write("---")
    st.header("Testing F.M.M.")


uploaded_file = st.file_uploader("Please upload your image")
if uploaded_file:
    #data = uploaded_file.getvalue()

    #image = pipe(prompt="make it pretty", image=data)
    #st.image(image)
    data = uploaded_file.getvalue()
    st.image(data)

def text():
    text = st.text_input("Please enter what you would like your uploaded image to look like (ex.: Jennifer Lawrence, happy, American...): ")
    print(text)
    return text


text()


import PIL
import requests
import torch
from io import BytesIO

from diffusers import StableDiffusionInstructPix2PixPipeline

def execute():
    prompt = text()
    def download_image(url):
        response = requests.get(url)
        return PIL.Image.open(BytesIO(response.content)).convert("RGB")


    # img_url = "https://huggingface.co/datasets/diffusers/diffusers-images-docs/resolve/main/mountain.png"

    # image = download_image(img_url).resize((512, 512))
    # image = PIL.Image.open('WhatsApp Image 2024-02-08 at 1.20.44 PM.jpeg').resize((512, 512))

    pipe = StableDiffusionInstructPix2PixPipeline.from_pretrained(
        "timbrooks/instruct-pix2pix", torch_dtype=torch.float32
    )
    # pipe = pipe.to("cuda")

#     jenni="https://goldenglobes.com/wp-content/uploads/2023/10/Jennifer-Lawrence-Photo.png"
# # imJenni = download_image(jenni).resize((512, 512))
#     imJenni = download_image(jenni).resize((512, 512))
#     # img = PIL.Image.open(uploaded_file)
#     prompt1 = "Make this person look Canadian"
    print("reached here")
    image = PIL.Image.open(uploaded_file).resize((512,512))
    img = pipe(prompt=prompt, image=image).images[0]

    print('executed')
    PIL.show(img)

st.button("execute", on_click=execute)
