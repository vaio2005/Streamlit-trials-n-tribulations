import streamlit as st
import requests
import time

st.set_page_config(
    page_title="BlackJack",
    page_icon=":spades:",
)

st.title("BlackJack")

st.header("What is this?")

st.markdown("""This is a simple app that uses the [Deck of Cards API](https://deckofcardsapi.com/) to play BlackJack.""")

def init():
    st.session_state['deck_id'] = ""
    st.session_state['player_balance'] = 100
    st.session_state['player_bet'] = 0
    st.session_state['game_state'] = "pre"


def create_deck():
    data = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
    data = data.json()
    st.session_state['deck_id'] = data['deck_id']

def draw_player_card():
    data = requests.get(f"https://deckofcardsapi.com/api/deck/{st.session_state['deck_id']}/draw/?count=1")
    data = data.json()
    playerHand = requests.get(f"https://deckofcardsapi.com/api/deck/{st.session_state['deck_id']}/pile/player/add/?cards={data['cards'][0]['code']}")
    playerHand = playerHand.json()
    if (playerHand['success'] != True):
        st.exception("Error adding card to player hand")
        return False

def draw_dealer_card():
    data = requests.get(f"https://deckofcardsapi.com/api/deck/{st.session_state['deck_id']}/draw/?count=1")
    data = data.json()
    dealerHand = requests.get(f"https://deckofcardsapi.com/api/deck/{st.session_state['deck_id']}/pile/dealer/add/?cards={data['cards'][0]['code']}")
    dealerHand = dealerHand.json()
    if (dealerHand['success'] != True):
        st.exception("Error adding card to dealer hand")
        return False

def calculate_player_hand():
    data = requests.get(f"https://deckofcardsapi.com/api/deck/{st.session_state['deck_id']}/pile/player/list/")
    data = data.json()
    cards = data['piles']['player']['cards']
    total = 0
    ace = False
    for card in cards:
        if (card['value'] == 'ACE'):
            ace = True
            total += 11
        elif (card['value'] == 'KING' or card['value'] == 'QUEEN' or card['value'] == 'JACK'):
            total += 10
        else:
            total += int(card['value'])
    if (ace == True and total > 21):
        total -= 10
    return total

def calculate_dealer_hand(first:bool):
    data = requests.get(f"https://deckofcardsapi.com/api/deck/{st.session_state['deck_id']}/pile/dealer/list/")
    data = data.json()
    cards = data['piles']['dealer']['cards']
    total = 0
    ace = False
    for card in cards:
        if (card['value'] == 'ACE'):
            ace = True
            total += 11
        elif (card['value'] == 'KING' or card['value'] == 'QUEEN' or card['value'] == 'JACK'):
            total += 10
        else:
            total += int(card['value'])
    if (ace is True and total > 21):
        total -= 10
    if (total == 21): return total
    if (first is True):
        if (cards[1]['value'] == 'KING' or cards[1]['value'] == 'QUEEN' or cards[1]['value'] == 'JACK'):
            total -= 10
        elif (cards[1]['value'] == 'ACE'):
            total -= 11
        else:
            total -= int(cards[1]['value'])
    return total

def get_player_hand():
    data = requests.get(f"https://deckofcardsapi.com/api/deck/{st.session_state['deck_id']}/pile/player/list/")
    data = data.json()
    cards = data['piles']['player']['cards']
    return cards

def get_dealer_hand():
    print(f"Getting dealer hand: {st.session_state['deck_id']}")
    print(f"URL: https://deckofcardsapi.com/api/deck/{st.session_state['deck_id']}/pile/dealer/list/")
    data = requests.get(f"https://deckofcardsapi.com/api/deck/{st.session_state['deck_id']}/pile/dealer/list/")
    data = data.json()
    cards = data['piles']['dealer']['cards']
    return cards

def clear_hands():

    data = requests.get(f"https://deckofcardsapi.com/api/deck/{st.session_state['deck_id']}/shuffle")
    data = data.json()
    if (data['success']  is not True):
        st.exception("Error shuffling deck")
        print(data)
        return False
    return True

if 'deck_id' not in st.session_state:
    init()
    create_deck()

if (st.session_state.get('deck_id') == ""):
    create_deck()

if (st.session_state.get('game_state') == "pre"):
    st.markdown("Welcome to BlackJack!")
    st.markdown("You have $100 to start with.")
    st.markdown(f"Your current balance is ${st.session_state['player_balance']}.")
    st.markdown("Place your bet and click 'Deal' to begin.")
    st.markdown("Good luck!")
    bet = st.slider("Bet", min_value=0, max_value=st.session_state['player_balance'], value=0)
    st.session_state['player_bet'] = bet
    print(bet)
    print(st.session_state['player_bet'])
    st.session_state['player_balance'] -= bet
    if (st.button("Deal")):
        st.session_state['game_state'] = "first"
    if (st.button("Reset")):
        init()
        create_deck()
        clear_hands()

col1,col2 = st.columns(2)
if (st.session_state.get('game_state') == "first"):
    with col1:
        st.title("Dealer")
        draw_player_card()
        draw_dealer_card()
        draw_player_card()
        draw_dealer_card()
        dealerHand = get_dealer_hand()
        if (calculate_dealer_hand(True) != 21):
            st.image(dealerHand[0]['image'])
            st.image("https://deckofcardsapi.com/static/img/back.png")
            st.text(f"Dealer hand: {calculate_dealer_hand(True)}")
        else:
            st.image(dealerHand[0]['image'])
            st.image(dealerHand[1]['image'])
            st.text(f"Dealer Hand: {calculate_dealer_hand(True)}")
            st.text("Dealer has Blackjack!")
            st.session_state['game_state'] = "end"
    
    with col2:
        st.title("Player")
        playerHand = get_player_hand()
        if (calculate_player_hand() != 21):
            st.image(playerHand[0]['image'])
            st.image(playerHand[1]['image'])
            st.text(f"Player Hand: {calculate_player_hand()}")
            if (st.button("Hit")):
                draw_player_card()
                st.session_state['game_state'] = "second"
            if (st.button("Stand")):
                st.session_state['game_state'] = "stand"
            
        else:
            st.image(playerHand[0]['image'])
            st.image(playerHand[1]['image'])
            st.text(f"Player Hand: {calculate_player_hand()}")
            st.text("Player has Blackjack!")
            st.session_state['player_balance'] += st.session_state['player_bet'] * 2.5
            st.session_state['game_state'] = "end"
        
if (st.session_state.get('game_state') == "second"):
    with col1:
        st.title("Dealer")
        dealerHand = get_dealer_hand()
        if (calculate_dealer_hand(True) != 21):
            st.image(dealerHand[0]['image'])
            st.image("https://deckofcardsapi.com/static/img/back.png")
            st.text(f"Dealer hand: {calculate_dealer_hand(True)}")
        else:
            st.image(dealerHand[0]['image'])
            st.image(dealerHand[1]['image'])
            st.text(f"Dealer Hand: {calculate_dealer_hand(True)}")
            st.text("Dealer has Blackjack!")
            st.session_state['game_state'] = "end"
    
    with col2:
        st.title("Player")
        playerHand = get_player_hand()
        if (calculate_player_hand() != 21):
            st.image(playerHand[0]['image'])
            st.image(playerHand[1]['image'])
            st.image(playerHand[2]['image'])
            st.text(f"Player Hand: {calculate_player_hand()}")
            if (calculate_player_hand() > 21):
                st.text("Player has busted!")
                st.session_state['game_state'] = "end"
            else:
                if (st.button("Hit")):
                    draw_player_card()
                    st.session_state['game_state'] = "third"
                if (st.button("Stand")):
                    st.session_state['game_state'] = "stand"
            
        else:
            st.image(playerHand[0]['image'])
            st.image(playerHand[1]['image'])
            st.image(playerHand[2]['image'])
            st.text(f"Player Hand: {calculate_player_hand()}")
            st.text("Player has Blackjack!")
            st.session_state['player_balance'] += st.session_state['player_bet'] * 2
            st.session_state['game_state'] = "end"

if (st.session_state.get('game_state') == "third"):
    with col1:
        st.title("Dealer")
        dealerHand = get_dealer_hand()
        if (calculate_dealer_hand(True) != 21):
            st.image(dealerHand[0]['image'])
            st.image("https://deckofcardsapi.com/static/img/back.png")
            st.text(f"Dealer hand: {calculate_dealer_hand(True)}")
        else:
            st.image(dealerHand[0]['image'])
            st.image(dealerHand[1]['image'])
            st.text(f"Dealer Hand: {calculate_dealer_hand(True)}")
            st.text("Dealer has Blackjack!")
            st.session_state['game_state'] = "end"
    
    with col2:
        st.title("Player")
        playerHand = get_player_hand()
        if (calculate_player_hand() != 21):
            st.image(playerHand[0]['image'])
            st.image(playerHand[1]['image'])
            st.image(playerHand[2]['image'])
            st.image(playerHand[3]['image'])
            st.text(f"Player Hand: {calculate_player_hand()}")
            if (calculate_player_hand() > 21):
                st.text("Player has busted!")
                st.session_state['game_state'] = "end"
            else:
                if (st.button("Hit", disabled=True)):
                    draw_player_card()
                    st.session_state['game_state'] = "fourth"
                if (st.button("Stand")):
                    st.session_state['game_state'] = "stand"
            
        else:
            st.image(playerHand[0]['image'])
            st.image(playerHand[1]['image'])
            st.image(playerHand[2]['image'])
            st.image(playerHand[3]['image'])
            st.text(f"Player Hand: {calculate_player_hand()}")
            st.text("Player has Blackjack!")
            st.session_state['player_balance'] += st.session_state['player_bet'] * 2
            st.session_state['game_state'] = "end"
            
if (st.session_state.get('game_state') == "stand"):
    while calculate_dealer_hand(False) < 17:
        draw_dealer_card()
        time.sleep(5)
    
    print(st.session_state.get('player_bet'))
    
    if (calculate_dealer_hand(False) > 21):
        st.text("Dealer has busted!")
        st.session_state['player_balance'] = st.session_state['player_balance'] + (st.session_state['player_bet'] * 2)
        st.session_state['game_state'] = "end"
    elif (calculate_dealer_hand(False) > calculate_player_hand()):
        st.text("Dealer has won!")
        st.session_state['game_state'] = "end"
    elif (calculate_dealer_hand(False) == calculate_player_hand()):
        st.text("It's a tie!")
        st.session_state['player_balance'] = st.session_state['player_balance'] + st.session_state['player_bet']
        st.session_state['game_state'] = "end"
    else:
        st.text("Player has won!")
        st.session_state['player_balance'] = st.session_state['player_balance'] + (st.session_state['player_bet'] * 2)
        st.session_state['game_state'] = "end"
    
    with col1:
        for card in dealerHand:
            st.image(card['image'])
        st.text(f"Dealer Hand: {calculate_dealer_hand(False)}")

    with col2:
        for card in playerHand:
            st.image(card['image'])
        st.text(f"Player Hand: {calculate_player_hand()}")
    
if (st.session_state.get('game_state') == "end"):
    if (st.button("Play Again")):
        st.session_state['game_state'] = "pre"
        st.session_state['player_bet'] = 0
        clear_hands()
