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
major_arcana = []
major_arcana_names = ["0. The Fool", "I. The Magician", "II. The High Priestess", "III. The Empress", "IV. The Emperor", "V. The Hierophant", "VI. The Lovers", "VII. The Chariot", "VIII. Strength", "IX. The Hermit", "X. Wheel of Fortune", "XI. Justice", "XII. The Hanged Man", "XIII. Death", "XIV. Temperance", "XV. The Devil", "XVI. The Tower", "XVII. The Star", "XVIII. The Moon", "XIX. The Sun", "XX. Judgement", "XXI. The World"]

# Create and add Major Arcana cards to the deck
for i, name in enumerate(major_arcana_names):
	card = Card(technotarot, name, i)
	major_arcana.append(card)
	technotarot.cards.append(card)

# Define the four suits of the Minor Arcana
suits = ["Pentacles", "Cups", "Swords", "Wands"]

# Define the pip (numbered) and face cards
pips = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
faces = ["Page", "Knight", "Queen", "King"]

# Create and add Minor Arcana cards to the deck
minor_arcana = []

for s in suits:
	# Add the numbered cards (Ace through Ten)
	for i, p in enumerate(pips):
		card = Card(technotarot, f"{p} of {s}", -(i + 1), s)
		minor_arcana.append(card)
		technotarot.cards.append(card)
	
	# Add the court (face) cards
	for i, f in enumerate(faces):
		card = Card(technotarot, f"{f} of {s}", -(i + 11), s)
		minor_arcana.append(card)
		technotarot.cards.append(card)