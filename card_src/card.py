class Card:
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def __repr__(self):
        return "{0} of {1}".format(self.rank, self.suit)


class NumberCard(Card):
    def __init__(self, rank, suit):
        super().__init__(str(rank), suit)


class AceCard(Card):
    def __init__(self, rank, suit):
        super().__init__('A', suit)


class FaceCard(Card):
    def __init__(self, rank, suit):
        super().__init__({11: 'J', 12: 'Q', 13: 'K'}[rank], suit)
