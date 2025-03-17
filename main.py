from random import randint

CARDS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
SUITS = ["♥", "♦", "♠", "♣"]

deck_of_cards = [f"{card}{suit}" for card in CARDS for suit in SUITS]
print(deck_of_cards)
print(len(deck_of_cards))

# Implement a solution for shuffling a deck of cards
# Use only randint() and no other imports
def shuffle_deck(deck_of_cards):
    shuffled_cards_list = []

    end_range = 51
    for i in range(len(deck_of_cards)):
        
        random_index = randint(0, end_range)
        random_card = deck_of_cards.pop(random_index)
        shuffled_cards_list.append(random_card)
        end_range -=1

    return shuffled_cards_list



shuffled_deck = shuffle_deck(deck_of_cards)
print(shuffled_deck)
# print(len(shuffled_deck))