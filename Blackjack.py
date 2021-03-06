from Deck import Deck
from Hand import Hand
import time


class Blackjack:

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.start()

    def start(self):
        while True:
            if input('New round? (Y or N): ').upper() == 'Y':
                self.play_round()
            else:
                print('Exiting')
                break

    def display(self, p_hand, d_hand):
        dealer_values = d_hand.hand_value()
        player_values = p_hand.hand_value()
        num_dealer_values = len(dealer_values)
        num_player_values = len(player_values)

        print('                      ')
        print('----------------------')
        print(f'Dealer: {d_hand} (', end='')
        for i, value in enumerate(dealer_values):
            if num_dealer_values > i + 1:
                print(f'{value} or ', end='')
            else:
                print(f'{value})')

        print(f'Player: {p_hand} (', end='')
        for i, value in enumerate(player_values):
            if num_player_values > i + 1:
                print(f'{value} or ', end='')
            else:
                print(f'{value})')
        print('----------------------')

    def play_round(self):
        p_hand = Hand(self.deck.deal_double())
        d_hand = Hand(self.deck.deal_double(deal_type='dealer'))

        p_final = 0

        while min(p_hand.hand_value()) < 21:
            self.display(p_hand, d_hand)
            if input('Hit or Stay? (H or S)').upper() == 'H':
                p_hand.add_card(self.deck.deal())
                if len(p_hand.hand_value()) == 0:
                    p_final = 0
                    break
            else:
                p_final = max(p_hand.hand_value())
                break

        time.sleep(3)

        d_hand.cards[1].flip()
        self.display(p_hand, d_hand)
        print(f'Dealer flipped a {d_hand.cards[1]}')

        d_final = 0

        while max(d_hand.hand_value()) < p_final:
            time.sleep(3)
            card = self.deck.deal()
            d_hand.add_card(card)
            self.display(p_hand, d_hand)
            print(f'Dealer flipped a {card}')
            if len(d_hand.hand_value()) == 0:
                d_final = 0
                break
            else:
                d_final = max(d_hand.hand_value())

        self.display(p_hand, d_hand)
        if p_final > d_final:
            print('Game Over: Player wins')
        elif d_final > p_final:
            print('Game Over: Dealer wins')
        else:
            print('Game Over: Push')
