import streamlit as st
import requests

st.set_page_config(
    page_title="API Example",
    page_icon=":satellite_antenna:",
)

st.title("API Exercise")

st.header("What is an API?")

st.markdown("""An API, literally, is an *Application Programming Interface*.  
Let's say that you want to perform an action on youtube, for example get the title of a video.  
You have two options:  
- scraping the website, which is unreliable and can break at any time (because the website changes, for example)  
- Using the API, which is a set of functions that you can call to perform actions on the website.  
Let's see an example of an API request.  """)

pokemon = st.text_input("Name of pokemon (undercase)", value="pikachu")

if st.button("Get pokemon"):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    st.text(f"This is the url we are going to use to get the pokemon data from pokeapi.co: \n{url}")
    response = requests.get(url)
    st.text("This is the reponse we get from pokeapi.co\n\nExpand at your risk, it contains a LOT of data.")
    st.json(response.json(), expanded=False)
    st.text("Let's get some detailed information.\nFor example the ID (Pokedex ID), height, weight, and the types.")
    st.text(f"ID: {response.json()['id']}")
    st.text("Height: " + str(response.json()['height']))
    st.text("Weight: " + str(response.json()['weight']))
    st.text("Types: " + ", ".join([t['type']['name'] for t in response.json()['types']]))
    st.text("Let's get the image sprite of the pokemon, shall we?")
    st.image(response.json()['sprites']['front_default'])
    st.text("This is a simple example, and there is a lot more data that is available.")
    st.text("With all of this data, you can do whatever you prefer!")
    st.text("But let's see the code behind all of this \"black magic\"")
    st.code("""
pokemon = st.text_input("Name of pokemon (undercase)", value="pikachu")

if st.button("Get pokemon"):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    st.text(f"This is the url we are going to use to get the pokemon data from pokeapi.co: \n{url}")
    response = requests.get(url) # This is where we ask the API and get the information back.
    #We're going to ignore some outputs, let's see directly the ID, height, weight, and types.
    height = response.json()['height'] # This takes the "height" key from the json response
    weight = response.json()['weight'] # This takes the "weight" key from the json response
    #Now the types are complex. A pokemon can have multiple types, so we need to get a list of the types, then join the types together with a comma.
    #So follow me here:
    # response.json()['types'] is a list of objects. Each object has a key called "type", which contains another object with a key called "name". That's what we're looking for.
    # So we're going to loop through the list, and for each object, we're going to get the "name" key from the "type" key.
    # We're going to do this by using a list comprehension, which is a fancy way of saying "for each object in the list, get the name key from the type key".
    types = ", ".join([t['type']['name'] for t in response.json()['types']])
    
    #The image is actually easier, since it's just an url, that we can use directly in the st.image function.
    image = response.json()['sprites']['front_default']
    st.image(image) #Easy!
    #To display the information, st.text() (or if you're fancy st.markdown()) is the way to go.
    """)