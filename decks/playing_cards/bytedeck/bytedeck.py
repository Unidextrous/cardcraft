# Add the parent directory to the system path to allow importing from cardcraft
import sys, os
bytedeck_dir = os.path.dirname(os.path.abspath(__file__))
playing_cards_dir = os.path.dirname(bytedeck_dir)
decks_dir = os.path.dirname(playing_cards_dir)
cardcraft_dir = os.path.dirname(decks_dir)
sys.path.append(cardcraft_dir)

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
	playing_cards.append(Card(bytedeck, f"Ace of {s}", "A", s, suits[s]))
	# Add the pip cards (Two through Ten)
	for i, p in enumerate(pips):
		card = Card(bytedeck, f"{p} of {s}", i + 2, s, suits[s])
		playing_cards.append(card)
	
	# Add the face cards
	for i, f in enumerate(faces):
		card = Card(bytedeck, f"{f} of {s}", f[0], s, suits[s])
		playing_cards.append(card)

jokers = []

jokers.append(Card(bytedeck, "Colored Joker", "🎨", None, "🃏"))
jokers.append(Card(bytedeck, "Black-and-White Joker", "✏️", None, "🃏"))

bytedeck.add_cards(playing_cards)

while True:
	choice = input("Add jokers? (y/n): ")
	if choice.lower() == "y":
		bytedeck.add_cards(jokers)
		break
	elif choice.lower() == "n":
		break
	print("Invalid choice")