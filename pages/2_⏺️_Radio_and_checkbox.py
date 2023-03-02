import streamlit as st

st.set_page_config(
    page_title="Radio and checkboxes",
    page_icon=":record_button:",
    layout="wide",
)

st.title("Radio and checkboxes")

st.header("Radio inputs")

st.write("Radio inputs are used to select one option from a list of options.")
st.write("Here is an example of a radio input:")

radio_input = st.radio(
    label="Choose an option",
    options=["Option 1", "Option 2", "Option 3"],
)
st.write(f"You selected: {radio_input}")

st.write("It's like magic, right?")
st.write("Let's see the code behind this:")

st.code("""
radio_input = st.radio(
    label="Choose an option",
    options=["Option 1", "Option 2", "Option 3"],
)
st.write(f"You selected: {radio_input}")
""", language="python")

st.write("That was easy enough, right?")

st.header("Checkboxes")

st.write("Checkboxes are used to select one or more options from a list of options.")
st.write("Here is an example of a checkbox:")
checkbox_input = st.checkbox(label="Check this box")
st.write(f"You checked: {checkbox_input}")

st.write("Let's see the code behind this:")

st.code("""
checkbox_input = st.checkbox(label="Check this box")
st.write(f"You checked: {checkbox_input}")
""", language="python")

st.write("Very easy! Now, let's see how to use checkboxes to select multiple options.")

st.write("Here is an example of a multiple selection checkbox:")
checkbox_input = st.multiselect(
    label="Select one or more options",
    options=["Option 1", "Option 2", "Option 3"],
)
st.write(f"You selected: {checkbox_input}")

st.write("Let's see the code behind this:")

st.code("""
checkbox_input = st.multiselect(
    label="Select one or more options",
    options=["Option 1", "Option 2", "Option 3"],
)
st.write(f"You selected: {checkbox_input}")
""", language="python")

st.write("That's it for this story. Thank you for reading!")
