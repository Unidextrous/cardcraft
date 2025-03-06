"""
technotarot.py

This script defines a TechnoTarot deck using the Card and Deck classes from the cardcraft module.
It initializes all Major and Minor Arcana cards and adds them to the deck.
"""


# Add the parent directory to the system path to allow importing from cardcraft
import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from cardcraft import Card, Deck

# Create the TechnoTarot deck
technotarot = Deck("TechnoTarot")

# Define the 22 Major Arcana cards (each with a unique name and index)
trump_cards = {
	"0. The Fool": "🃏0.",
	"I. The Magician": "♾️I.",
	"II. The High Priestess": "🔮II.",
	"III. The Empress": "👸III.",
	"IV. The Emperor": "🤴IV.",
	"V. The Hierophant": "⛪V.",
	"VI. The Lovers": "💕VI.",
	"VII. The Chariot": "🏇VII.",
	"VIII. Strength": "💪VIII.",
	"IX. The Hermit": "🔦IX.",
	"X. Wheel of Fortune": "🔄X.",
	"XI. Justice": "⚖️XI.",
	"XII. The Hanged Man": "🪢XII.",
	"XIII. Death": "💀XIII.",
	"XIV. Temperance": "🏺XIV.",
	"XV. The Devil": "😈XV.",
	"XVI. The Tower": "⚡XVI",
	"XVII. The Star": "🌟XVII.",
	"XVIII. The Moon": "🌙XVIII.",
	"XIX. The Sun": "☀️XIX.",
	"XX. Judgement": "🎺XX.",
	"XXI. The World": "🌎XXI."
}

# Create and add Major Arcana cards to the deck
major_arcana = []

for i, name in enumerate(trump_cards):
	card = Card(technotarot, name, "", "Major Arcana", trump_cards[name])
	major_arcana.append(card)

technotarot.add_cards(major_arcana)

# Create and add Minor Arcana cards to the deck
minor_arcana = []

# Define the four suits of the Minor Arcana
suits = {
	"Pentacles": "🪙", "Cups": "🍵", "Swords": "⚔️", "Wands": "🪄"
}

# Define the pip (numbered) and face cards
pips = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
faces = ["Page", "Knight", "Queen", "King"]

# Create and add Minor Arcana cards to the deck
for s in suits:
	minor_arcana.append(Card(technotarot, f"Ace of {s}", "A", s, suits[s]))
	# Add the numbered cards (Two through Ten)
	for i, p in enumerate(pips):
		card = Card(technotarot, f"{p} of {s}", str(i + 2), s, suits[s])
		minor_arcana.append(card)
	
	# Add the court (face) cards
	for i, f in enumerate(faces):
		if f == "Knight":
			card = Card(technotarot, f"{f} of {s}", "N", s, suits[s])
		else:
			card = Card(technotarot, f"{f} of {s}", f[0], s, suits[s])
		minor_arcana.append(card)

technotarot.add_cards(minor_arcana)