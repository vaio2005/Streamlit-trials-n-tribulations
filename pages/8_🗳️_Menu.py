import streamlit as st

st.set_page_config(
    page_title="Menu",
    page_icon=":ballot_box:",
    layout="centered",
)

st.title("Menu")

st.write("In streamlit there are two types of menus: single choiche or multiple choiche. In this section we will see how to use both of them.")

st.header("Single choiche menu")

st.write("To create a single choiche menu you can use the `st.selectbox()` function. This function takes as input a label, a list of options and a default value. The default value is the value that will be selected when the page is loaded.")

st.code("""
st.selectbox(
    label="Choose a SuperHero",
    options=["Batman", "Superman", "Spiderman", "Ironman", "Thor"],
    index=0,
)
""", language="python")

st.write("The `index` parameter is optional and it is used to select the default value. If you don't specify it, the first value of the list will be selected.")

st.write("The `st.selectbox()` function returns the selected value.")

st.write("Here's what that will look like (plus an output with your choice): ")

option = st.selectbox(
    label="Choose a SuperHero",
    options=["Batman", "Superman", "Spiderman", "Ironman", "Thor"],
    index=0,
)

st.write(f"You selected: {option}")

st.header("Multiple choiche menu")

st.write("To create a multiple choiche menu you can use the `st.multiselect()` function. This function takes as input a label, a list of options and a default value. The default value is the value that will be selected when the page is loaded.")

st.code("""
st.multiselect(
    label="Choose your favorite SuperHeroes",
    options=["Batman", "Superman", "Spiderman", "Ironman", "Thor"],
    default=["Batman", "Ironman"],
)
""", language="python")

st.write("The `default` parameter is optional and it is used to select the default values. If you don't specify it, no values will be selected.")

st.write("The `st.multiselect()` function returns a list with the selected values.")

st.write("Here's what that will look like (plus an output with your choices): ")

options = st.multiselect(
    label="Choose your favorite SuperHeroes",
    options=["Batman", "Superman", "Spiderman", "Ironman", "Thor"],
    default=["Batman", "Ironman"],
)

st.write(f"You selected: {options}")

