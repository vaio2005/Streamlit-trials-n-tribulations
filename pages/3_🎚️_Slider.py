import streamlit as st
from datetime import datetime, time, timedelta

st.set_page_config(
    page_title="Slider",
    page_icon=":level_slider:",
    layout="wide",
)

st.title("Slider")

st.write("A slider is used to select a value from a range of values.")
st.write("Here is an example of a slider:")

slider_input = st.slider(
    label="Magic level :sparkles:",
    min_value=0,
    max_value=100,
    value=50,
    step=1,
)

st.write(f"You selected: {slider_input}")

st.write("For example, this slider has a minimum value of 0, a maximum value of 100, a default value of 50, and a step of 1.")
st.write("Let's see the code behind this:")

st.code("""
slider_input = st.slider(
    label="Magic level :sparkles:",
    min_value=0,
    max_value=100,
    value=50,
    step=1,
)
""", language="python")

st.write("That was easy enough, right?")

st.write("But wait, there's more!")

st.write("You can also use a slider to select a value with a custom step size.")

st.write("Here is an example of a slider with a custom step size:")
slider_input = st.slider(
    label="Magic level :sparkles:",
    min_value=0.0,
    max_value=100.0,
    value=50.0,
    step=0.1,
)

st.write(f"You selected: {slider_input}")

st.write("For example, this slider has a minimum value of 0.0, a maximum value of 100.0, a default value of 50.0, and a step of 0.1.")
st.write("Let's see the code behind this:")
st.code("""
slider_input = st.slider(
    label="Magic level :sparkles:",
    min_value=0.0,
    max_value=100.0,
    value=50.0,
    step=0.1,
)
""", language="python")

st.write("And now a slider to select a range of values.")
slider_input = st.slider(
    label="Acceptable level of magic :sparkles:",
    min_value=0,
    max_value=100,
    value=(25, 75),
    step=1,
)

st.write(f"You selected: {slider_input}")

st.write("For example, this slider has a minimum value of 0, a maximum value of 100, a default value of (25, 75), and a step of 1.")
st.write("Let's see the code behind this:")

st.code("""
slider_input = st.slider(
    label="Acceptable level of magic :sparkles:",
    min_value=0,
    max_value=100,
    value=(25, 75),
    step=1,
)
""", language="python")

st.write("You can also use a slider to select a date. Here is an example of that:")
slider_input = st.slider(
    label="When were you born?",
    min_value=datetime(1950, 1, 1),
    max_value=datetime(2023, 1, 1),
    value=datetime(2000, 1, 1),
    step=timedelta(days=1),
    format="DD/MM/YYYY",
)

st.write(f"You selected: {slider_input}")

st.write("For example, this slider has a minimum value of 1950-01-01, a maximum value of 2023-01-01, a default value of 2000-01-01, and a step of 1 day.")
st.write("Let's see the code behind this:")

st.code("""
slider_input = st.slider(
    label="When were you born?",
    min_value=datetime(1950, 1, 1),
    max_value=datetime(2023, 1, 1),
    value=datetime(2000, 1, 1),
    step=timedelta(days=1),
    format="DD/MM/YYYY",
)
""", language="python")

st.write("This type of slider also requires the `datetime` module to be imported.")

#Setting here the correct timezone



st.write("Last but not least, you can also use a slider to select a time. Here is an example of that:")
st.write("While we're at this, let's see if you can select the right time.")
st.write("Right now, it's: :clock12: " + datetime.utcnow().strftime("%H:%M") + " UTC")

slider_input = st.slider(
    label="What UTC time is it?",
    min_value=time(0, 0, 0),
    max_value=time(23, 59, 59),
    value=time(12, 0, 0),
    step=timedelta(minutes=1),
    format="HH:mm",
)

st.write(f"You selected: {slider_input}")
if slider_input.hour != datetime.utcnow().hour:
    st.write("That's not the right time!")
elif slider_input.minute != datetime.utcnow().minute:
    st.write("That's not the right time!")
else:
    st.write("That's the right time! :tada:")
    st.balloons()
st.write("For example, this slider has a minimum value of 00:00:00, a maximum value of 23:59:59, a default value of 12:00:00, and a step of 1 minute.")
st.write("Let's see the code behind this:")
st.code("""
slider_input = st.slider(
    label="What time is it?",
    min_value=time(0, 0, 0),
    max_value=time(23, 59, 59),
    value=time(12, 0, 0),
    step=timedelta(minutes=1),
    format="HH:mm",
)
""", language="python")

st.write("This type of slider also requires the `time` and `timedelta` modules to be imported.")

st.write("That's all for now. Thanks for reading!")