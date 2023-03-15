import streamlit as st 
import requests

st.set_page_config(
    page_title="Pokemon Stats",
    page_icon=":space_invader:",
)

@st.cache_data
def get_pokemon(pokemon):
    return requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}").json()

st.title("Which pokemon is the best?")

st.header("What is this?")
st.markdown("""This is a simple app that uses the [PokeAPI](https://pokeapi.co/) to get information about pokemon. We've learned how to use it in the previous section, so let's use it to get some information about pokemon.""")

pokemon1 = st.text_input("Name of pokemon 1 (undercase)", value="pikachu")
pokemon2 = st.text_input("Name of pokemon 2 (undercase)", value="charmander")

pokemon1 = get_pokemon(pokemon1)
pokemon2 = get_pokemon(pokemon2)

col1, col2 = st.columns(2, gap="large")

#grab the stats of the pokemons
pokemon1_stats = pokemon1['stats']
pokemon2_stats = pokemon2['stats']

#grab the hp of the pokemons
pokemon1_hp = pokemon1_stats[0]['base_stat']
pokemon2_hp = pokemon2_stats[0]['base_stat']

#grab the attack of the pokemons
pokemon1_attack = pokemon1_stats[1]['base_stat']
pokemon2_attack = pokemon2_stats[1]['base_stat']

#grab the defense of the pokemons
pokemon1_defense = pokemon1_stats[2]['base_stat']
pokemon2_defense = pokemon2_stats[2]['base_stat']

#grab the special attack of the pokemons
pokemon1_special_attack = pokemon1_stats[3]['base_stat']
pokemon2_special_attack = pokemon2_stats[3]['base_stat']

#grab the special defense of the pokemons
pokemon1_special_defense = pokemon1_stats[4]['base_stat']
pokemon2_special_defense = pokemon2_stats[4]['base_stat']

#grab the speed of the pokemons
pokemon1_speed = pokemon1_stats[5]['base_stat']
pokemon2_speed = pokemon2_stats[5]['base_stat']


with col1:
    st.header(pokemon1['name'].title())
    col11, col12, col13 = st.columns(3)
    with col11:
        st.metric(label="HP", value=pokemon1_hp, delta=pokemon1_hp - pokemon2_hp)
        st.metric(label="Attack", value=pokemon1_attack, delta=pokemon1_attack - pokemon2_attack)
    with col12:
        st.metric(label="Defense", value=pokemon1_defense, delta=pokemon1_defense - pokemon2_defense)
        st.metric(label="Special Attack", value=pokemon1_special_attack, delta=pokemon1_special_attack - pokemon2_special_attack)
    with col13:
        st.metric(label="Special Defense", value=pokemon1_special_defense, delta=pokemon1_special_defense - pokemon2_special_defense)
        st.metric(label="Speed", value=pokemon1_speed, delta=pokemon1_speed - pokemon2_speed)


with col2:
    st.header(pokemon2['name'].title())
    col21,col22,col23 = st.columns(3)
    with col21:
        st.metric(label="HP", value=pokemon2_hp, delta=pokemon2_hp - pokemon1_hp)
        st.metric(label="Attack", value=pokemon2_attack, delta=pokemon2_attack - pokemon1_attack)
    with col22:
        st.metric(label="Defense", value=pokemon2_defense, delta=pokemon2_defense - pokemon1_defense)
        st.metric(label="Special Attack", value=pokemon2_special_attack, delta=pokemon2_special_attack - pokemon1_special_attack)
    with col23:
        st.metric(label="Special Defense", value=pokemon2_special_defense, delta=pokemon2_special_defense - pokemon1_special_defense)
        st.metric(label="Speed", value=pokemon2_speed, delta=pokemon2_speed - pokemon1_speed)


if (pokemon1_hp + pokemon1_attack + pokemon1_defense + pokemon1_special_attack + pokemon1_special_defense + pokemon1_speed) > (pokemon2_hp + pokemon2_attack + pokemon2_defense + pokemon2_special_attack + pokemon2_special_defense + pokemon2_speed):
    st.success(f"{pokemon1['name'].title()} is better")
else:
    st.success(f"{pokemon2['name'].title()} is better")