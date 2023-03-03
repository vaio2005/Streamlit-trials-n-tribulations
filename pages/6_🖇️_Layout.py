import streamlit as st

st.set_page_config(
    page_title="Layout",
    page_icon=":paperclips:",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Grab a random meme from reddit using meme-api.com
def grab_meme_url():
    import requests
    import json

    ups = 0
    url = "https://meme-api.com/gimme/wholesomememes"
    while ups < 300:
        response = requests.get(url)
        data = json.loads(response.text)
        ups = data['ups']
    meme = data['url'] + "?width=250"
    return meme

st.title("Layout")

st.write("Streamlit has a few different layouts that you can choose from.")
st.write("We've already seen the sidebar, which is where you choose the page you want to see.")

st.write("But let's see the other layouts.")

col1, col2, col3 = st.columns(3);

with col1:
    st.header("This is a column")
    st.write("You can put anything in a column, like a button.")
    st.button("Click me!", on_click=st.balloons())

with col2:
    st.header("This is another column")
    st.write("You can also put an image in a column.")
    st.image(grab_meme_url(), use_column_width=True)

with col3:
    import time
    st.header("This is another column")
    st.write("Or also a progress bar.")
    progress_text = "I'm absorbing the memes..."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    

st.write("There's also a \"tabs\" layout, let's see how that looks.")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Meme 1", "Meme 2", "Meme 3", "Meme 4", "Meme 5"])

with tab1:
    st.image(grab_meme_url(), width=350)
    time.sleep(1)

with tab2:
    st.image(grab_meme_url(), width=350)
    time.sleep(1)

with tab3:
    st.image(grab_meme_url(), width=350)
    time.sleep(1)

with tab4:
    st.image(grab_meme_url(), width=350)
    time.sleep(1)

with tab5:
    st.image(grab_meme_url(), width=350)
    time.sleep(1)

st.write("")
st.write("")
st.write("You can also have some text hidden, let's see that now.")

expander = st.expander("Click here to see the hidden text")
expander.write(":mage: You shall not pass! :mage:")

st.write("")
st.write("")
st.write("")
st.write("And this is the end for it all. Thanks for reading!")