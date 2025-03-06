# Add the parent directory to the system path to allow importing from cardcraft
import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from cardcraft import Card, Deck

# Create the ByteDeck deck
bytedeck = Deck("ByteDeck")

suits = {
    "Spades": "♠️",
    "Hearts": "♥️",
    "Diamonds": "♦️",
    "Clubs": "♣️"
}

# Define the pip (numbered) and face cards
pips = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
faces = ["Jack", "Queen", "King"]

# Create and add Minor Arcana cards to the deck
playing_cards = []

for s in suits:
	playing_cards.append(Card(bytedeck, f"Ace of {s}", "Ace", s, f"{suits[s]}A"))
	# Add the pip cards (Two through Ten)
	for i, p in enumerate(pips):
		card = Card(bytedeck, f"{p} of {s}", i + 2, s, f"{suits[s]}{i + 2}")
		playing_cards.append(card)
	
	# Add the face cards
	for i, f in enumerate(faces):
		card = Card(bytedeck, f"{f} of {s}", (i + 11), s, f"{suits[s]}{f[0]}")
		playing_cards.append(card)

jokers = []

for i in range(2):
	if i == 0:
		name = "Colored Joker"
		representation = "🃏🎨"
	else:
		name = "Black-and-White Joker"
		representation = "🃏✏️"
	jokers.append(Card(bytedeck, name, 0, None, representation))

bytedeck.add_cards(playing_cards)