from card_src.card import NumberCard, FaceCard, AceCard
import random

class Deck:
    def __init__(self):
        self.cards = []

    def init_with_cards(self):
        for rank in range(1, 14):
            for suit in ('Clubs', 'Diamonds', 'Hearts', 'Spades'):
                if rank == 1:
                    self.cards.append(AceCard(rank, suit))
                elif 2 <= rank < 11:
                    self.cards.append(NumberCard(rank, suit))
                elif 11 <= rank < 14:
                    self.cards.append(FaceCard(rank, suit))
                else:
                    raise IndexError("Invalid rank!!")

    def deal(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)
