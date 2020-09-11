import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):

# MVP
    
    def setUp(self):
        self.guest_1 = Guest("David", 150, "Jolene")
        self.guest_2 = Guest("Kyle", 100, "Lovers")
        self.guest_3 = Guest("Antonia", 200, "I should be so lucky")
        self.guest_4 = Guest("Ewen", 50, "We will rock you")

    def test_guest_name(self):
        self.assertEqual("Antonia", self.guest_3.name)

    def test_guest_wallet(self):
        self.assertEqual(100, self.guest_2.wallet) 

    def test_guest_favourite_song(self):
        self.assertEqual("We will rock you", self.guest_4.favourite_song) 

