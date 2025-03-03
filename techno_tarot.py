from cardcraft import Card, Deck

tt_deck = Deck("TechnoTarot")

major_arcana = []

major_arcana_names = ["0. The Fool", "I. The Magician", "II. The High Priestess", "III. The Empress", "IV. The Emperor", "V. The Hierophant", "VI. The Lovers", "VII. The Chariot", "VIII. Strength", "IX. The Hermit", "X. Wheel of Fortune", "XI. Justice", "XII. The Hanged Man", "XIII. Death", "XIV. Temperance", "XV. The Devil", "XVI. The Tower", "XVII. The Star", "XVIII. The Moon", "XIX. The Sun", "XX. Judgement", "XXI. The World"]

for i, name in enumerate(major_arcana_names):
	card = Card(tt_deck, name, i)
	major_arcana.append(card)

suits = ["Pentacles", "Cups", "Swords", "Wands"]

pips = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
		
faces = ["Page", "Knight", "Queen", "King"]

minor_arcana = []

for s in suits:
	for i, p in enumerate(pips):
		card = Card(tt_deck, f"{p} of {s}", -(i + 1), s)
		minor_arcana.append(card)
	for i, f in enumerate(faces):
		card = Card(tt_deck, f"{f} of {s}", -(i + 11), s)
		minor_arcana.append(card)
		
tt_deck.cards = major_arcana + minor_arcana

tt_deck.bridge_shuffle()
print(tt_deck.cards)