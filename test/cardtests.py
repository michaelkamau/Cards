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
        Should be able to create an object of Card class
        """
        spade_card = NumberCard(4, 'Spade')
        self.assertIsInstance(spade_card, NumberCard)

    def test_can_create_FaceCard_object(self):
        """
        Should be able to create an object of Card class
        """
        face_card = FaceCard(11, 'Hearts')
        self.assertIsInstance(face_card, FaceCard)
