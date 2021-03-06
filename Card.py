class Card:

    SUITS = ('H', 'C', 'S', 'D')
    RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
    VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
              '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': (1, 11)}

    def __init__(self, rank, suit, visible=True):
        self.visible = visible
        self.rank = rank
        self.value = Card.VALUES[rank]
        self.suit = suit

    def __str__(self):
        return f'{self.rank}{self.suit}'

    def flip(self):
        self.visible = not self.visible

