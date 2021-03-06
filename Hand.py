from Card import Card


class Hand:

    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        string = ''
        for card in self.cards:
            if card.visible:
                string += card.__str__() + ' '
            else:
                string += 'XX' + ' '
        return string

    def add_card(self, card):
        self.cards.append(card)

    def hand_value(self):
        values = [0]
        for card in self.cards:
            if card.visible:
                if card.rank == 'A':
                    values.extend(values)
                    for i, value in enumerate(values):
                        if i < len(values)/2:
                            values[i] += card.value[0]
                        else:
                            values[i] += card.value[1]
                else:
                    for i, value in enumerate(values):
                        values[i] += card.value
        for value in values:
            if value > 21:
                values.remove(value)
        return tuple(set(values))
