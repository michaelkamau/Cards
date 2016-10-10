import unittest
from card_src.card import Card, AceCard, FaceCard, NumberCard


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
        ace_card = Card(1, 'Diamonds')
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
        n = NumberCard(5,'Hearts')
        self.assertEqual('5 of Hearts', repr(n))

    def test_string_repr_AceCard(self):
        """
        AceCard should have correct string repr
        """
        a = AceCard(1, 'Spades')
        self.assertEqual('A of Spades', repr(a))
