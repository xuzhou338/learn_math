from random import shuffle


class Card:
    def __init__(self, n=1):
        """n is the number of decks, and each deck has 52 cards by default."""
        self.cards = list(range(1, 53))*n

    def card_read(self, card_code):
        if card_code <= 13:
            suit = 'spades'
            rank = card_code
        elif card_code > 13 and card_code <= 26:
            suit = 'clubs'
            rank = card_code - 13
        elif card_code > 26 and card_code <= 39:
            suit = 'hearts'
            rank = card_code - 26
        else:
            suit = 'diamonds'
            rank = card_code - 39
        return suit, rank

    def shuffle(self):
        shuffle(self.cards)
        print('The deck(s) is shuffled!')

    def draw_card(self, m=-1):
        card_code = self.cards[m]
        suit, rank = self.card_read(card_code)
        print('You drew {0} of {1}'.format(rank, suit))

    def display(self):
        for card_code in self.cards:
            suit, rank = self.card_read(card_code)
            print('{0} of {1}'.format(rank, suit))

if __name__ == '__main__':
    card1 = Card()
    card1.shuffle()
    card1.draw_card()
