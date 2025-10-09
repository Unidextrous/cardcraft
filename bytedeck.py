from cardcraft_core import Card, Deck

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
	playing_cards.append(Card(f"Ace of {s}", "A", s, suits[s]))
	# Add the pip cards (Two through Ten)
	for i, p in enumerate(pips):
		card = Card(f"{p} of {s}", i + 2, s, suits[s])
		playing_cards.append(card)
	
	# Add the face cards
	for i, f in enumerate(faces):
		card = Card(f"{f} of {s}", f[0], s, suits[s])
		playing_cards.append(card)

bytedeck.cards += playing_cards

jokers = []

jokers.append(Card("Colored Joker", "🎨", None, "🃏"))
jokers.append(Card("Black-and-White Joker", "✏️", None, "🃏"))

while True:
	choice = input("Add jokers? (y/n)\n\n>>> ")
	if choice.lower() == "y":
		bytedeck.cards += jokers
		break
	elif choice.lower() == "n":
		break
	print("Invalid choice\n")

bytedeck.finalize_init()