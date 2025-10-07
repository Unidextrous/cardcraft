from cardcraft_core import Card, Deck

# Create the Rider-Waite deck
rider_waite = Deck("Rider-Waite")

# Define the 22 Major Arcana
trump_cards = [
    ("0. The Fool", "🃏", 0),
    ("I. The Magician", "♾️", 1),
    ("II. The High Priestess", "🔮", 2),
    ("III. The Empress", "👸", 3),
    ("IV. The Emperor", "🤴", 4),
    ("V. The Hierophant", "⛪", 5),
    ("VI. The Lovers", "💕", 6),
    ("VII. The Chariot", "🏇", 7),
    ("VIII. Strength", "💪", 8),
    ("IX. The Hermit", "🔦", 9),
    ("X. Wheel of Fortune", "🔄", 10),
    ("XI. Justice", "⚖️", 11),
    ("XII. The Hanged Man", "🪢", 12),
    ("XIII. Death", "💀", 13),
    ("XIV. Temperance", "🏺", 14),
    ("XV. The Devil", "😈", 15),
    ("XVI. The Tower", "⚡", 16),
    ("XVII. The Star", "🌟", 17),
    ("XVIII. The Moon", "🌙", 18),
    ("XIX. The Sun", "☀️", 19),
    ("XX. Judgement", "🎺", 20),
    ("XXI. The World", "🌎", 21),
]

major_arcana = [Card(name, value, "Major Arcana", symbol) for name, symbol, value in trump_cards]
rider_waite.cards += major_arcana

# Define the Minor Arcana
suits = {
    "Wands": "🪄",
    "Cups": "🍵",
    "Swords": "⚔️",
    "Pentacles": "🪙"
}

pips = ["Ace"] + [str(i) for i in range(2, 11)]
faces = ["Page", "Knight", "Queen", "King"]

minor_arcana = []
for suit, symbol in suits.items():
    # Pips
    for value, pip in enumerate(pips, start=1):
        minor_arcana.append(Card(f"{pip} of {suit}", value, suit, symbol))
    # Faces
    for i, face in enumerate(faces, start=11):
        minor_arcana.append(Card(f"{face} of {suit}", i, suit, symbol))

rider_waite.cards += minor_arcana

rider_waite.finalize_init()