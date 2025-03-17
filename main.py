from random import randint

CARDS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
SUITS = ["♥", "♦", "♠", "♣"]

deck_of_cards = [f"{card}{suit}" for card in CARDS for suit in SUITS]

# Implement a solution for shuffling a deck of cards
# Use only randint() and no other imports
def shuffle_deck(deck_of_cards):
    pass
