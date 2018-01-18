from collections import namedtuple

class Card(namedtuple('Card', ['rank', 'suit'])):
    """
    A card class with rank and suit.
    """
    __slots__ = ()
    """
    Using namedtupleand slots allows us to not use __init__. Like a constructor function so that we're not calling the Card class 52 times.
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    """

    def __repr__(self):
        return f"{self.__class__.__name__}({self.rank}, {self.suit})"

class Deck:

    ranks = [str(i) for i in range(2, 11)] + list('JQKA')
    suits = ['heart', 'diamond', 'spade', 'club']

    def __init__(self):
        """
        self.cards = []
        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append(Card(rank, suit))
        """
        self.cards = [Card(rank, suit)  for suit in self. suits
                                        for rank in self. ranks]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, index):
        return self.cards[index]

if __name__ == "__main__":
    print("Hello World")
