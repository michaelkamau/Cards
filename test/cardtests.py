import unittest
from card_src.card import Card, AceCard, FaceCard, NumberCard
from card_src.hand import Hand
from card_src.deck import Deck

class IndividualCardsTests(unittest.TestCase):
    def test_can_create_card_object(self):
        """
        Should be able to create an object of Card class
        """
        spade_card = Card(4, 'Spade')
        self.assertIsInstance(spade_card, Card)

    def test_can_create_NumberCard_object(self):
        """
        Should be able to create an object of NumberCard class
        """
        spade_card = NumberCard(4, 'Spade')
        self.assertIsInstance(spade_card, NumberCard)

    def test_can_create_FaceCard_object(self):
        """
        Should be able to create an object of FaceCard class
        """
        face_card = FaceCard(11, 'Hearts')
        self.assertIsInstance(face_card, FaceCard)

    def test_can_create_AceCard_object(self):
        """
        Should be able to create an object of AceCard class
        """
        ace_card = AceCard(1, 'Diamonds')
        self.assertIsInstance(ace_card, AceCard)

    def test_subclasses_of_card_are_card_objects(self):
        """
        The subclasses of Card class i.e FaceCard, AceCard and NumberCard should be instances of Card
        """
        a, b, c = (NumberCard(5, 'Diamonds'), FaceCard(12, 'Hearts'), AceCard(1, 'Spades'))
        self.assertIsInstance(a, Card) and self.assertIsInstance(b, Card) and self.assertIsInstance(c, Card)

    def test_string_repr_for_card(self):
        """
        Should have the correct string repr
        """
        h = Card(4, "Spades")
        self.assertEqual('4 of Spades', repr(h))

    def test_string_repr_NumberCard(self):
        """
        NumberCard should have the correct string repr
        """
        n = NumberCard(5, 'Hearts')
        self.assertEqual('5 of Hearts', repr(n))

    def test_string_repr_AceCard(self):
        """
        AceCard should have correct string repr
        """
        a = AceCard(1, 'Spades')
        self.assertEqual('A of Spades', repr(a))

    def test_string_repr_FaceCard(self):
        """
        FaceCard should have correct string repr
        """
        f = FaceCard(13, 'Diamonds')
        self.assertEqual('K of Diamonds', repr(f))


class IndividualHandTests(unittest.TestCase):
    def test_can_create_hand_object(self):
        """
        Should be able to create an object of Hand class
        """
        h = Hand()
        self.assertIsInstance(h, Hand)

    def test_can_get_number_cards_at_hand(self):
        """
        Should be able to get number of cards at hand
        """
        g = Hand()
        self.assertEqual(0, g.get_cards_held())


    def test_can_add_cards_at_hand(self):
        """
        Should be able to add cards to Hand object
        """
        h = Hand()
        s_card = NumberCard(5, 'Spades')
        h.add_card(s_card)
        self.assertEqual(1, h.get_cards_held())

    def test_can_remove_card_from_hand(self):
        """
        Should be able to remove a card from hand
        """
        h = Hand()
        c1 = AceCard(1, 'Diamonds')
        c2 = FaceCard(13, 'Diamonds')

        h.add_card(c1)
        h.add_card(c2)

        h.remove_card(c2)

        self.assertEqual(1, h.get_cards_held())


class IndividualDeckTests(unittest.TestCase):
    def test_can_create_deck_object(self):
        """
        Should be able to create an instance of Deck class
        """
        d = Deck()
        self.assertIsInstance(d, Deck)

    def test_initialize_deck_with_cards(self):
        """
        Should be able to initialize a deck with 52 cards
        """
        d = Deck()
        d.init_with_cards()
        self.assertEqual(52, len(d.cards))

    def test_can_deal_a_card(self):
        """
        Should be able to remove a card from deck
        """
        d = Deck()
        d.init_with_cards()
        new_card = d.deal()
        self.assertEqual(51, len(d.cards))


if __name__ == '__main__':
    unittest.main()