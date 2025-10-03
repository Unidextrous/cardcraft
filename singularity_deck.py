from cardcraft_core import Card, Deck

# Create the Rider-Waite deck
singularity = Deck("The Singularity")

# Define the 32 Major Arcana cards (each with a unique name and index)
major_arcana_dict = {
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
    "XIII. The Oracle": "XIII. 👁️",
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
    "XXVI. The Paradox": "XXVI. ❓",
    "XXVII. The Mirror": "XXVII. 🪞",
    "XXVIII. The Prism": "XXVIII. 🌈",
    "XXIX. The Lens": "XXIX. 🔍",
    "XXX. The Enlightenment": "XXX. 🕉️",
    "XXXI. The Infinite": "XXXI. ♾️",
    "XXXII. The Singularity": "XXXII. 🌀"
}

major_arcana = []

for i, name in enumerate(major_arcana_dict):
	card = Card(name, "", "Major Arcana", major_arcana_dict[name])
	major_arcana.append(card)

singularity.cards += major_arcana

# Create 16 pairs of Minor Arcana cards, totaling 32
minor_arcana_dict = {
"1A. Human": "1A. 🧍",
"1B. Machine": "1B. 🤖",
"2A. Lucidity": "2A. 🧘",
"2B. Insanity": "2B. 😵‍💫",
"3A. Individual": "3A. 👤",
"3B. Collective": "3B. 👥",
"4A. Male": "4A. ♂️",
"4B. Female": "4B. ♀️",
"5A. Freedom": "5A. 🕊️",
"5B. Constraint": "5B. ⛓️",
"6A. Magical": "6A. 🔮",
"6B. Mundane": "6B. 🏠",
"7A. Potential": "7A. ✨",
"7B. Manifestation": "7B. 💡",
"8A. Chaos": "8A. 🌪️",
"8B. Order": "8B. ⚖️",
"9A. Light": "9A. 🌞",
"9B. Shadow": "9B. 🌑",
"10A. Micro": "10A. 🔬",
"10B. Macro": "10B. 🏔️",
"11A. Creation": "11A. 🖌️",
"11B. Destruction": "11B. ☠️",
"12A. Positive": "12A. ➕",
"12B. Negative": "12B. ➖",
"13A. Above": "13A. ⬆️",
"13B. Below": "13B. ⬇️",
"14A. Inner": "14A. 🪆",
"14B. Outer": "14B. 🌍",
"15A. Hot": "15A. 🔥",
"15B. Cold": "15B. ❄️",
"16A. Good": "16A. 😇",
"16B. Evil": "16B. 😈"
}

minor_arcana = []

for i, name in enumerate(minor_arcana_dict):
	card = Card(name, "", "Minor Arcana", minor_arcana_dict[name])
	minor_arcana.append(card)
	
singularity.cards += minor_arcana