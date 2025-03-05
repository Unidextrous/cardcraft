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
	"0.": "The Fool",
	"I.": "The Magician",
	"II.": "The High Priestess",
	"III.": "The Empress",
	"IV.": "The Emperor",
	"V.": "The Hierophant",
	"VI.": "The Lovers",
	"VII.": "The Chariot",
	"VIII.": "Strength",
	"IX.": "The Hermit",
	"X.": "Wheel of Fortune",
	"XI.": "Justice",
	"XII.": "The Hanged Man",
	"XIII.": "Death",
	"XIV.": "Temperance",
	"XV.": "The Devil",
	"XVI.": "The Tower",
	"XVII.": "The Star",
	"XVIII.": "The Moon",
	"XIX.": "The Sun",
	"XX.": "Judgement",
	"XXI.": "The World"
}

# Create and add Major Arcana cards to the deck
major_arcana = []

for i, rank in enumerate(trump_cards):
	card = Card(technotarot, f"{rank} {trump_cards[rank]}", i, representation=rank)
	major_arcana.append(card)

technotarot.add_cards(major_arcana)

# Create and add Minor Arcana cards to the deck
minor_arcana = []

# Define the four suits of the Minor Arcana
suits = {
	"Pentacles": "🪙", "Cups": "💧", "Swords": "🗡️", "Wands": "🪄"
}

# Define the pip (numbered) and face cards
pips = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
faces = ["Page", "Knight", "Queen", "King"]

# Create and add Minor Arcana cards to the deck
for s in suits:
	# Add the numbered cards (Ace through Ten)
	for i, p in enumerate(pips):
		if i == 0:
			card = Card(technotarot, f"Ace of {s}", 1, s, f"{suits[s]}A")
		else:
			card = Card(technotarot, f"{p} of {s}", (i + 1), s, f"{suits[s]}{i + 1}")
		minor_arcana.append(card)
	
	# Add the court (face) cards
	for i, f in enumerate(faces):
		if f == "Knight":
			card = Card(technotarot, f"{f} of {s}", (i + 11), s, f"{suits[s]}N")
		else:
			card = Card(technotarot, f"{f} of {s}", (i + 11), s, f"{suits[s]}{f[0]}")
		minor_arcana.append(card)

technotarot.add_cards(minor_arcana)