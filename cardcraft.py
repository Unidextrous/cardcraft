import sys
import random

def choose_index(prompt, min_val, max_val):
	"""Helper method to get a valid index input from the user."""
	while True:
		try:
			index = int(input(prompt))
			if min_val <= index <= max_val:
				return index
			print("Invalid input.")
		except ValueError:
			print(f"Invalid input. Please enter an integer.")

class Card:
	"""Represents a single playing card with properties such as value, suit, and orientation."""

	def __init__(self, home_deck, name, value, suit=None,face_up=False, orientation="upright"):
		self.home_deck = home_deck # The deck this card originally belongs to
		self.name = name # Card name (e.g. Ace of Spades)
		self.value = value # Card value (e.g. 1 for Ace, 11 for Jack, etc.)
		self.suit = suit # Suit of the card (Hearts, Diamonds, etc.), if applicable
		self.face_up = face_up # Whether the card is face-up or face-down
		self.orientation = orientation # Card orientation (upright or reversed)
	
	def __repr__(self):
		return self.name # String representation of the card

class Deck:
	"""Represents a deck of cards, which can be split into sub-decks and merged back."""
	def __init__(self, name, id="0", cards=None, parent=None):
		"""
		Initializes a deck.

        :param name: The name of the deck (e.g., "Playing Cards", "Uno Deck", etc.)
        :param id: A unique identifier representing the deck's position in the hierarchy
        :param parent: The parent deck (None if this is the root deck)
        :param cards: The list of cards in the deck
		"""
		self.name = name #
		self.id = id # Binary-like ID to track sub-decks
		self.cards = cards if cards is not None else [] # List of cards in this deck
		self.parent = parent # Parent deck (if any)
		self.children = [] # List of sub-decks (children)
		
		# Prevent decks with invalid names from being created
		if self.parent == None and ("0" in name or "1" in name):
			print(name, "is not a valid name for a deck")
			sys.exit()
	
	def get_root(self):
		"""Finds the root (topmost) deck in the hierarchy."""
		current = self
		while current.parent:
			current = current.parent
		return current
		
	def get_deck(self, id):
		"""
		Retrieves a sub-deck based on its ID.

		:param id: The binary-style ID string indicating the path to the deck
		:return: The corresponding Deck object
		"""
		root = self.get_root()  # Always start from the root
		current = root  # Start traversal from the root deck
        
        # Traverse down the tree using the ID's binary structure
		for bit in id[1:]:  # Ignore the first character (root is always "0")
			if len(current.children) > int(bit):  # Ensure valid index
				current = current.children[int(bit)]
			else:
				return None  # Return None if the path does not exist
		return current
	
	def add_subdeck(self, id, cards):
		"""
		Creates a sub-deck and adds it to the current deck.

		:param id: The binary-style ID string indicating the path to the deck
		:param cards: The list of cards to be added to the sub-deck
		"""
		if self.get_deck(id):
			print("Deck already exists")
			return
		subdeck = Deck(self.name, id, cards, self) # Create two sub-decks from the current deck
		subdeck.parent = self # Set the current deck as the sub-deck's parent deck
		self.children.append(subdeck) # Add the sub-deck to the parent deck
			
	def randomize(self):
		"""Shuffles the deck's cards randomly."""
		random.shuffle(self.cards)
	
	def split_choice(self):
		"""
		Asks the user whether to manually choose a split index or let the system choose randomly.

		:return: The chosen split index
		"""
		choice = choose_index(f"1. Choose index\n2. Randomly select\n>>> ", 1, 2)
		if choice == 1:
			return choose_index(f"Please enter a split index between 0 and {len(self.cards)}\n>>> ", 0, len(self.cards))
		elif choice == 2:
			return random.randint(0, len(self.cards))
				
	def split(self, index=None):
		"""
		Splits the deck into two sub-decks at the given index.

		:param index: The index at which to split the deck - if None, asks user for input
		"""
		if index is None:
			index = self.split_choice()
		
		self.add_subdeck(self.id + "0", self.cards[:index])
		self.add_subdeck(self.id + "1", self.cards[index:])
		
	def stack(self, top_deck):
		"""
		Stacks a deck onto the current deck

		"""
		self.cards = top_deck.cards + self.cards
		
		if top_deck.parent:
			parent = top_deck.parent
			sibling = parent.children[0] if parent.children[1] is top_deck else parent.children[1]
			parent.cards = sibling.cards
			parent.children = []
	
	def cut(self):
		"""Performs a cut by splitting and then merging the sub-decks back."""
		self.split()
		self.children[0].stack(self.children[1])
		
	def overhand_shuffle(self):
		"""Simulates an overhand shuffle by repeatedly taking small portions from the top of the bottom sub-deck and stacking them onto the top one."""
		pass
	
	def riffle_shuffle(self):
		"""Simulates a riffle shuffle by splitting the deck into two halves at a slightly varied midpoint."""
	
	def hindu_shuffle(self):
		"""Simulates a Hindu shuffle by repeatedly taking small portions from the top of the deck and stacking them onto the hand."""
		pass
		
	def __repr__(self):
		return f"{self.name}#{self.id}: {self.cards}" # String representation of the deck