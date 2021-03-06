from Deck import Deck
from Hand import Hand
import time


class Blackjack:

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.balance = 0
        self.start()

    def start(self):

        while True:
            self.balance = input("How much would you like to deposit?: ")
            try:
                self.balance = int(self.balance)
                break
            except ValueError:
                print('Invalid deposit, please enter a number')
                continue

        while True:
            print(f'Balance: {self.balance}')
            bet = input('Enter your bet amount to play again (N to quit): ')

            if bet.upper() == 'N':
                print(f'Exiting with ${self.balance}')
                break
            elif bet.isdigit():
                bet = float(bet)
                if bet > self.balance:
                    print('Insufficient funds, try again')
                    continue
                else:
                    print(f'Betting ${bet}')
                    self.balance -= bet
                    self.balance += self.play_round(bet)
            else:
                print('Invalid bet, please enter a number')
                continue

    def display(self, p_hand, d_hand):
        dealer_values = d_hand.hand_value()
        player_values = p_hand.hand_value()
        num_dealer_values = len(dealer_values)
        num_player_values = len(player_values)

        print('                      ')
        print(f'Balance: {self.balance}')
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

    def play_round(self, bet):
        p_hand = Hand(self.deck.deal_double())
        d_hand = Hand(self.deck.deal_double(deal_type='dealer'))

        p_final = 0

        while True:
            self.display(p_hand, d_hand)
            if input('Hit or Stay? (H or S)').upper() == 'H':
                p_hand.add_card(self.deck.deal())
                status = p_hand.check_hand()
                if status == 'bust':
                    p_final = 0
                    break
                elif status == 'blackjack':
                    p_final = 21
                    break
                else:
                    continue
            else:
                p_final = max(p_hand.hand_value())
                break

        time.sleep(3)

        d_hand.cards[1].flip()
        self.display(p_hand, d_hand)
        print(f'Dealer flipped a {d_hand.cards[1]}')

        while max(d_hand.hand_value()) < 17 and max(d_hand.hand_value()) < p_final:
            time.sleep(3)
            card = self.deck.deal()
            d_hand.add_card(card)
            self.display(p_hand, d_hand)
            status = d_hand.check_hand()
            print(f'Dealer flipped a {card}')
            if status == 'bust':
                d_final = 0
                break
            elif status == 'blackjack':
                d_final = 21
                break
            else:
                continue
        else:
            d_final = max(d_hand.hand_value())

        self.display(p_hand, d_hand)
        if p_final > d_final and p_hand.bust is False:
            print('Game Over: Player wins')
            self.return_hands(p_hand, d_hand)
            if p_final == 21:
                return bet * 2.5
            else:
                return bet * 2
        elif d_final > p_final and d_hand.bust is False:
            print('Game Over: Dealer wins')
            self.return_hands(p_hand, d_hand)
            return 0
        else:
            print('Game Over: Push')
            self.return_hands(p_hand, d_hand)
            return bet

    def return_hands(self, p_hand, d_hand):
        self.deck.to_reserve(p_hand.cards)
        self.deck.to_reserve(d_hand.cards)
