# cardcraft_divination.py

from cardcraft.cardcraft_core import Deck, Card

class Position:
    """
    Represents a single position in a spread.
    Can hold a card and has an optional meaning (e.g. 'Past', 'Present').
    """
    def __init__(self, name: str, meaning: str = None):
        self.name = name
        self.meaning = meaning
        self.card = None

    def place_card(self, card: Card):
        self.card = card

    def __repr__(self):
        meaning = f" ({self.meaning})" if self.meaning else ""
        card = f" -> {self.card}" if self.card else " -> [empty]"
        return f"{self.name}{meaning}{card}"


class Spread:
    """
    Represents a spread of cards used for divination.
    Contains multiple positions that can be filled with drawn or 'jumped' cards.
    """
    def __init__(self, name: str, positions: list[str]):
        self.name = name
        self.positions = [Position(pos) for pos in positions]

    def deal(self, deck: Deck, messy: bool = False):
        """
        Deals cards into the spread. Uses normal draws by default,
        but can capture 'jumping' cards from messy shuffles too.
        """
        cards_to_place = []

        if messy:
            # gather any "fallen" cards from the shuffle
            for card in deck.overhand_shuffle(messy=True):
                cards_to_place.append(card)

        # fill any remaining positions with normal draws
        while len(cards_to_place) < len(self.positions) and len(deck.cards) > 0:
            cards_to_place.append(deck.draw())

        # place them into the spread positions
        for pos, card in zip(self.positions, cards_to_place):
            pos.place_card(card)

    def __repr__(self):
        return f"{self.name} Spread:\n" + "\n".join(str(p) for p in self.positions)

