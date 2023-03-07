import streamlit as st
import time

st.set_page_config(
    page_title="Image Generation",
    page_icon=":art:",
    layout="centered",
)

# Convert the prompt to the correct format
# The format is: 
# scene + ",%20" + adjective + ",%20" + characters (with details) + ",%20" + adjective + ",%20"+ visual style (3 times, all separated by ",%20") + ",%20" + genre + ",%20" + artist reference
# We don't use a lot of the parameters, some are forced by code.
def convert_Prompt(scene: str, character: str):
    result = "" + scene + ",%20Beautiful,%20" + character + ",%20anime"
    result= result.replace(" ", "%20")
    return result.lower()



st.title("Image Generation")

st.write("Insert a prompt and the model will generate an image.")

scene = st.text_input(label="Scene", value="A beautiful sunset")
character = st.text_input(label="Character", value="Spiderman swinging on a web")




if st.button("Generate"):
    prompt = convert_Prompt(scene, character)
    with st.spinner("Generating image..."):
        time.sleep(5)
        markdown = f"""
        ![Generated image](https://image.pollinations.ai/prompt/{prompt})
        """

    st.markdown(markdown)
    st.write("This is the generated image.")
