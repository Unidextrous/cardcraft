# Add the parent directory to the system path to allow importing from cardcraft
import sys, os
rider_waite_dir = os.path.dirname(os.path.abspath(__file__))
tarot_dir = os.path.dirname(rider_waite_dir)
decks_dir = os.path.dirname(tarot_dir)
cardcraft_dir = os.path.dirname(decks_dir)
sys.path.append(cardcraft_dir)

from cardcraft import Card, Deck

# Create the Rider-Waite deck
rider_waite = Deck("Rider-Waite")

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
	card = Card(rider_waite, name, "", "Major Arcana", trump_cards[name])
	major_arcana.append(card)

rider_waite.add_cards(major_arcana)

# Create and add Minor Arcana cards to the deck
minor_arcana = []

# Define the four suits of the Minor Arcana
suits = {
	"Wands": "🪄", "Cups": "🍵", "Swords": "⚔️", "Pentacles": "🪙"
}

# Define the pip (numbered) and face cards
pips = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
faces = ["Page", "Knight", "Queen", "King"]

# Create and add Minor Arcana cards to the deck
for s in suits:
	minor_arcana.append(Card(rider_waite, f"Ace of {s}", "A", s, suits[s]))
	# Add the numbered cards (Two through Ten)
	for i, p in enumerate(pips):
		card = Card(rider_waite, f"{p} of {s}", str(i + 2), s, suits[s])
		minor_arcana.append(card)
	
	# Add the court (face) cards
	for i, f in enumerate(faces):
		if f == "Knight":
			card = Card(rider_waite, f"{f} of {s}", "N", s, suits[s])
		else:
			card = Card(rider_waite, f"{f} of {s}", f[0], s, suits[s])
		minor_arcana.append(card)

rider_waite.add_cards(minor_arcana)

print(rider_waite)