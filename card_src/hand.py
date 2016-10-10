class Hand:
    def __init__(self):
        self.card_at_hand = []

    def get_cards_held(self):
        return len(self.card_at_hand)
