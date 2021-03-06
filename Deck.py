from Card import Card
from random import shuffle


class Deck:

    def __init__(self):
        self.cards = []
        self.reserve = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.cards.append(Card(rank, suit))
        print('Deck has been initialized')

    def __str__(self):
        string = 'Deck: '
        for card in self.cards:
            string += card.__str__() + ' '
        return string

    def shuffle(self):
        shuffle(self.cards)
        print('Deck has been shuffled')

    def deal(self):
        if len(self.cards) == 0:
            self.refill_from_reserve()
        return self.cards.pop()

    def deal_double(self, deal_type='player'):
        if len(self.cards) == 0:
            self.refill_from_reserve()
        card1 = self.cards.pop()
        if len(self.cards) == 0:
            self.refill_from_reserve()
        card2 = self.cards.pop()

        if deal_type == 'dealer':
            card2.flip()

        double = [card1, card2]
        return double

    def to_reserve(self, cards):
        self.reserve.extend(cards)

    def refill_from_reserve(self):
        self.cards.extend(self.reserve)
        print('Refilling deck from reserve')
        self.shuffle()
        self.reserve.clear()
