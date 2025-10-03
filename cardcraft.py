import random

class Card:
	"""Represents a single playing card with properties such as value, suit, and orientation."""

	def __init__(self, name, value, suit=None, symbol=None, face_up=False, orientation="upright"):
		self.name = name # Card name (e.g. Ace of Spades)
		self.value = value # Card value (e.g. 1 for Ace, 11 for Jack, etc.)
		self.suit = suit # Suit of the card (Hearts, Diamonds, etc.), if applicable
		self.symbol = symbol # Symbol representing the suit (e.g., ♥, ♦, ♠, ♣)
		self.face_up = face_up # Whether the card is face-up or face-down
		self.orientation = orientation # Card orientation (upright or reversed)
	
	def rotate(self):
		"""Toggle orientation."""
		self.orientation = "reversed" if self.orientation == "upright" else "upright"

	def __repr__(self):
		return f"{self.symbol}{self.value}({self.orientation[0]})"

class Deck:
	def __init__(self, name, cards=None):
		self.name = name
		self.cards = cards or []
		self.original_order = list(self.cards)  # Keep a copy for resets

	def draw(self, n=1):
		"""Draw n cards from the top."""
		drawn = self.cards[:n]
		self.cards = self.cards[n:]
		return drawn
	
	def reverse(self):
		"""Reverse the deck order and rotate all cards."""
		self.cards.reverse()
		for card in self.cards:
			card.rotate()

	def cut(self, index=None):
		"""Cut the deck at a specific index or roughly in half."""
		if index is None:
			mid = len(self.cards) // 2
			variation = len(self.cards) // 8
			index = random.randint(mid - variation, mid + variation)
		self.cards = self.cards[index:] + self.cards[:index]

	def randomize(self):
		random.shuffle(self.cards)

	def overhand_shuffle(self, min_chunk=1, max_chunk=5, messy=False, drop_chance=0.1):
		"""
		Perform an overhand shuffle.

		:param min_chunk: Minimum number of cards to take at once
		:param max_chunk: Maximum number of cards to take at once
		:param messy: If True, some cards may "fall out" during the shuffle
		:param drop_chance: Probability of each card being dropped
		:return: List of cards that were dropped
		"""
		original = self.cards[:]
		shuffled = []
		dropped_cards = []

		while original:
			chunk_size = random.randint(min_chunk, max_chunk)
			chunk = original[:chunk_size]
			original = original[chunk_size:]

			if messy:
				remaining_chunk = []
				for card in chunk:
					if random.random() < drop_chance:
						dropped_cards.append(card)  # card falls out and is removed from the deck
					else:
						remaining_chunk.append(card)
				chunk = remaining_chunk

			shuffled = chunk + shuffled

		self.cards = shuffled
		return dropped_cards

	def bridge_shuffle(self, reverse=False):
		"""
		Perform a bridge (riffle) shuffle by splitting the deck in half and interleaving cards.

		:param reverse: If True, the bottom half is reversed and all cards rotated
		"""
		mid = len(self.cards) // 2
		top = self.cards[:mid]
		bottom = self.cards[mid:]

		if reverse:
			bottom.reverse()
			for card in bottom:
				card.rotate()

		shuffled = []
		while top or bottom:
			if top and (not bottom or random.random() > 0.5):
				shuffled.append(top.pop(0))
			elif bottom:
				shuffled.append(bottom.pop(-1))

		self.cards = shuffled

	def faro_shuffle(self, reverse=False):
		"""
		Perform a Faro shuffle by splitting the deck in half and perfectly interleaving the cards.
		
		:param reverse: If True, the bottom half is reversed and all cards rotated
		"""
		mid = len(self.cards) // 2
		top = self.cards[:mid]
		bottom = self.cards[mid:]

		if reverse:
			bottom.reverse()
			for card in bottom:
				card.rotate()
		
		bottom = bottom[::-1]

		shuffled = []
		# Interleave cards from top and bottom
		for t, b in zip(top, bottom):
			shuffled.append(t)
			shuffled.append(b)

		# If the deck has an odd number of cards, append the last remaining card
		if len(top) > len(bottom):
			shuffled.append(top[-1])
		elif len(bottom) > len(top):
			shuffled.append(bottom[-1])

		self.cards = shuffled


	def reset_order(self):
		"""Reset deck to original order and orientation."""
		self.cards = list(self.original_order)
		for card in self.cards:
			card.orientation = "upright"

	def __repr__(self):
		return f"<Deck {self.name}: {len(self.cards)} cards>"