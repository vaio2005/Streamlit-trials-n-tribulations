import streamlit as st
import requests
import json
import urllib.request


st.set_page_config(
    page_title="Download",
    page_icon=":floppy_disk:",
    layout="wide",
)

# Grab a random meme from reddit using meme-api.com
def grab_meme_url():

    ups = 0
    url = "https://meme-api.com/gimme/wholesomememes"
    while ups < 300:
        response = requests.get(url)
        data = json.loads(response.text)
        ups = data['ups']
    meme = data['url']
    return meme


st.title("Download")

st.header("How can I download a file from Streamlit?")

st.write("It's EASY! Just use the `st.download_button()` function!")

st.write("In fact, this button downloads a random meme!")
st.write("Want to try? Click the button below!")

url = grab_meme_url()
img_data = requests.get(url).content
btn = st.download_button(
    label="Download Meme",
    data=img_data,
    file_name="meme.jpg",
    mime="image/jpg",
)

st.write("The code for it is pretty simple too!")

st.code("""
with open("meme.png", "rb") as file:
    st.download_button(
        label="Download Meme",
        data=file,
        file_name="meme.png",
        mime="image/png",
    )
""")

st.write("This assumes that you have a file called `meme.png` in your current directory, but if you don't, you can use the `requests` library to download the image from the internet!")

st.code("""
url = "Your URL here, it should end with .jpg or .png"
img_data = requests.get(url).content
btn = st.download_button(
    label="Download Meme",
    data=img_data,
    file_name="meme.jpg", # or .png
    mime="image/jpg", # or .png
)
""")

