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

	def __init__(self, home_deck, name, value, suit=None, symbol=None, face_up=False, orientation="upright"):
		self.home_deck = home_deck # The deck this card originally belongs to
		self.name = name # Card name (e.g. Ace of Spades)
		self.value = value # Card value (e.g. 1 for Ace, 11 for Jack, etc.)
		self.suit = suit # Suit of the card (Hearts, Diamonds, etc.), if applicable
		self.symbol = symbol # Symbol representing the suit (e.g., ♥, ♦, ♠, ♣)
		self.face_up = face_up # Whether the card is face-up or face-down
		self.orientation = orientation # Card orientation (upright or reversed)
	
	def __repr__(self):
		return f"{self.symbol}{self.value}"

class Deck:
	"""Represents a deck of cards, which can be split into sub-decks, merged with another deck, or shuffled in various ways."""
	def __init__(self, name, id="", cards=None, parent=None):
		"""
		Initializes a deck.

        :param name: The name of the deck (e.g., "Playing Cards", "Uno Deck", etc.)
        :param id: A unique identifier representing the deck's position in the hierarchy
        :param parent: The parent deck (None if this is the root deck)
        :param cards: The list of cards in the deck
		"""
		self.name = name
		self.id = id # Binary-like ID to track sub-decks
		self.cards = cards if cards is not None else [] # List of cards in this deck
		self.parent = parent # Parent deck (if any)

		# If this is the root deck (i.e., parent is None), initialize the children attribute with a new sub-deck that has the same name, the ID "0", and the same cards as the parent deck.
		self.children = [Deck(self.name, "0", parent=self)] if parent is None else []
		
		# Prevent decks with invalid names from being created
		if self.parent == None and ("0" in name or "1" in name):
			print(name, "is not a valid name for a deck")
			sys.exit()
	
	def add_cards(self, new_cards):
		"""
		Adds multiple cards to the deck at once.
		
		:param new_cards: A list of cards to be added to the deck.
		"""
		self.cards = new_cards + self.cards

		if self.children:
			self.children[0].add_cards(new_cards)
	
	def get_root(self):
		"""Finds the root (topmost) deck in the hierarchy."""
		current = self
		while current.parent is not None:
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
		for bit in id:
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
			print(f"Deck#{id} already exists")
			return
		subdeck = Deck(self.name, id, cards, self) # Create two sub-decks from the current deck
		subdeck.parent = self # Set the current deck as the sub-deck's parent deck
		self.children.append(subdeck) # Add the sub-deck to the parent deck
	
	def randomize(self):
		"""Shuffles the deck's cards randomly."""
		
		random.shuffle(self.cards)

	def order(self):
		ordered_deck = self.get_root()
		self.get_deck("0").cards = ordered_deck.cards
	
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

		if len(self.children[0].cards) == 0 or len(self.children[1].cards) == 0:
			self.cards = self.children[0].cards + self.children[1].cards
			self.children = []
		
	def place_onto(self, bottom_deck):
		"""
		Places top_deck onto bottom_deck

		"""
		bottom_deck.cards = self.cards + bottom_deck.cards
		if self.parent:
			parent = self.parent

			# Identify the sibling deck (the other half of the split)
			if len(self.parent.children) == 2:
				sibling = parent.children[1] if parent.children[0] == self else parent.children[0]
			
				# The parent deck now takes on the sibling deck's cards
				parent.cards = sibling.cards

				# Clear the children list since the decks are merged back
				parent.children = []

	def cut(self, index=None):
		"""Performs a cut by splitting and then merging the sub-decks back."""
		if index == None:
			mid = len(self.cards) // 2
			variation =  len(self.cards) // 8
			index = random.randint(mid - variation, mid + variation)
		self.split(index)
		self.children[1].place_onto(self.children[0])
		
	def overhand_shuffle(self, index=None, chunk_range=None):
		"""Simulates an overhand shuffle by repeatedly taking small portions from the top of the bottom sub-deck and placing them onto the top one."""
		if chunk_range == None:
			chunk_range = [3, 9]
		
		if index == None:
			mid = len(self.cards) // 2
			variation =  len(self.cards) // 8
			index = random.randint(mid - variation, mid + variation)

		self.split(index)

		chunk_min = chunk_range[0]
		chunk_max = chunk_range[1]

		hand = self.get_deck(self.id + "1")
		while len(hand.cards) > 0:
			chunk_size = random.randint(chunk_min, chunk_max)
			hand.split(min(chunk_size, len(hand.cards) - 1))
			if len(hand.children) == 0:
				break
			hand.children[0].place_onto(self.children[0])
		hand.place_onto(self.children[0])

	def riffle_split(self, riffle_range):
		max_riffle_index = len(self.cards) - riffle_range[0]
		min_riffle_index = len(self.cards) - riffle_range[1]
		self.split(min(random.randint(min_riffle_index, max_riffle_index), len(self.cards)))
	
	def bridge_shuffle(self, index=None, riffle_range=None):
		"""Simulates a bridge shuffle by splitting the deck into two halves at a slightly varied midpoint."""
		if riffle_range == None:
			riffle_range = [1, 5]

		if index == None:
			mid = len(self.cards) // 2
			variation =  len(self.cards) // 8
			index = random.randint(mid - variation, mid + variation)
		
		self.split(index)
		subdeck0 = self.get_deck(self.id + "0")
		subdeck1 = self.get_deck(self.id + "1")

		subdeck0.riffle_split(riffle_range)

		subdeck00 = self.get_deck(subdeck0.id + "0")
		subdeck01 = self.get_deck(subdeck0.id + "1")

		while (len(self.children)) > 0:
			if len(subdeck0.children) > 0:
				if subdeck1:
					subdeck1.riffle_split(riffle_range)
					subdeck10 = self.get_deck(subdeck1.id + "0")
					subdeck11 = self.get_deck(subdeck1.id + "1")

					if subdeck11:
						subdeck11.place_onto(subdeck01)
					
				if subdeck00:
					subdeck00.riffle_split(riffle_range)
					subdeck000 = self.get_deck(subdeck00.id + "0")
					subdeck001 = self.get_deck(subdeck00.id + "1")

					if subdeck001:
						subdeck001.place_onto(subdeck01)
					else:
						subdeck00.place_onto(subdeck01)

			if len(subdeck0.children) == 0 and subdeck1:
				subdeck1.place_onto(subdeck0)
	
	def faro_shuffle(self):
		"""Simulates a Faro shuffle by splitting the deck into two equal halves and then interleaving the cards."""
		self.bridge_shuffle(len(self.cards) // 2, [1, 1])

	def shuffle(self):
		deck = self.get_deck("0")
		while True:
			choice = input("1. Order Deck\n2. Cut Deck\n3. Overhand Shuffle\n4. Bridge Shuffle\n5. Faro Shuffle\n6. Randomize\n7. End Shuffle\n>>> ")
			match choice:
				case "1":
					deck.order()
				case "2":
					deck.cut()
				case "3":
					deck.overhand_shuffle()
				case "4":
					deck.bridge_shuffle()
				case "5":
					deck.faro_shuffle()
				case "6":
					deck.randomize()
				case "7":
					break
			print(deck)

	def __repr__(self):
		if self.id:
			return f"{self.name}#{self.id}: {self.cards}"
		return f"{self.name} Home: {self.cards}"