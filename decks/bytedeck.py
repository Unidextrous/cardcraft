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
	# Add the numbered cards (Ace through Ten)
	for i, p in enumerate(pips):
		if i == 0:
			card = Card(bytedeck, f"Ace of {s}", 1, s, f"{suits[s]}A")
		else:
			card = Card(bytedeck, f"{p} of {s}", i + 1, s, f"{suits[s]}{i + 1}")
		playing_cards.append(card)
	
	# Add the face cards
	for i, f in enumerate(faces):
		card = Card(bytedeck, f"{f} of {s}", (i + 11), s, suits[s] + f[0])
		playing_cards.append(card)

bytedeck.add_cards(playing_cards)

print(bytedeck)