from cardcraft_core import Card, Deck

# Create the Rider-Waite deck
singularity = Deck("The Singularity")

# Define the 32 Major Arcana cards (each with a unique name and index)
arcana_prime_dict = {
    "I. The Source": "I. 🌌",
    "II. The Dreamer": "II. 🌙",
    "III. The Architect": "III. 📐",
    "IV. The Network": "IV. 🕸️",
    "V. The Matrix": "V. 🔢",
    "VI. The Silence": "VI. 🤫",
    "VII. The Melody": "VII. 🎵",
    "VIII. The Harmony": "VIII. 🎶",
    "IX. The Seeker": "IX. 🧭",
    "X. The Philosopher": "X. 💭",
    "XI. The Intelligence": "XI. 🧠",
    "XII. The Magician": "XII. 🪄",
    "XIII. The Oracle": "XIII. 🔮",
    "XIV. The Technomage": "XIV. 🧙‍♂️",
    "XV. The Programmer": "XV. 💻",
    "XVI. The Algorithm": "XVI. 📊",
    "XVII. The Circuit": "XVII. 🔌",
    "XVIII. The Flow": "XVIII. 🌊",
    "XIX. The Signal": "XIX. 📡",
    "XX. The Resistance": "XX. 🛑",
    "XXI. The Loop": "XXI. 🔄",
    "XXII. The Catalyst": "XXII. 💥",
    "XXIII. The Hacker": "XXIII. 🔧",
    "XXIV. The Cyborg": "XXIV. 🦾",
    "XXV. The Glitch": "XXV. ⚠️",
    "XXVI. The Paradox": "XXVI. 🤯",
    "XXVII. The Mirror": "XXVII. 🪞",
    "XXVIII. The Prism": "XXVIII. 🌈",
    "XXIX. The Lens": "XXIX. 🔍",
    "XXX. The Observer": "XXX. 👁️",
    "XXXI. The Infinite": "XXXI. ♾️",
    "XXXII. The Singularity": "XXXII. 🌀"
}

arcana_prime = []

for i, name in enumerate(arcana_prime_dict):
	card = Card(name, i + 1, "Arcana Prime", arcana_prime_dict[name])
	arcana_prime.append(card)

singularity.cards += arcana_prime

# Create 16 pairs of Minor Arcana cards, totaling 32
mirror_arcana_dict = {
    "1A. Creation": "1A. 🖌️",
    "2A. Light": "2A. 🌞",
    "3A. Simple": "3A. ⚪",
    "4A. Chaos": "4A. 🌪️",
    "5A. Potential": "5A. ✨",
    "6A. Constraint": "6A. ⛓️",
	"7A. Ignorance": "7A. ❔",
    "8A. Micro": "8A. 🔬",
    "9A. Individual": "9A. 👤",
    "10A. Organic": "10A. 🧬",
    "11A. Male": "11A. ♂️",
    "12A. Mundane": "12A. 🏠",
	"13A. Stagnation": "13A. 🏜️",
    "14A. Random": "14A. 🎲",
    "15A. Below": "15A. ⬇️",
    "16A. Inner": "16A. 🪆",
    "16B. Outer": "16B. 🌍",
    "15B. Above": "15B. ⬆️",
    "14B. Intentional": "14B. 🎯",
	"13B. Growth": "13B. 🌳",
    "12B. Magical": "12B. 🕯️",
    "11B. Artificial": "11B. 🤖",
    "10B. Collective": "10B. 👥",
    "9B. Female": "9B. ♀️",
    "8B. Macro": "8B. 🏔️",
	"7B. Knowledge": "7B. 📚",
    "6B. Freedom": "6B. 🕊️",
    "5B. Manifestation": "5B. 💡",
    "4B. Order": "4B. ⚖️",
    "3B. Complex": "3B. 🧩",
    "2B. Shadow": "2B. 🌑",
    "1B. Destruction": "1B. ☠️"
}

mirror_arcana = []

for i, name in enumerate(mirror_arcana_dict):
	if i < 16:
		value = 1 + i
	else:
		value = 32 - i
	card = Card(name, value, "Mirror Arcana", mirror_arcana_dict[name])
	mirror_arcana.append(card)
	
singularity.cards += mirror_arcana

singularity.finalize_init()