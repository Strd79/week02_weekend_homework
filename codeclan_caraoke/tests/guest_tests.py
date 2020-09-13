import unittest
from src.guest import Guest
from src.room import Room

class TestGuest(unittest.TestCase):

# MVP
    
    def setUp(self):
        self.guest_1 = Guest("David", 150, "Jolene")
        self.guest_2 = Guest("Kyle", 100, "Lovers")
        self.guest_3 = Guest("Antonia", 200, "I should be so lucky")
        self.guest_4 = Guest("Ewen", 300, "We will rock you")

        self.room_1 = Room("The Popaoke room", 10, 15)
        self.room_2 = Room("The Countryaoke room", 6, 20)
        self.room_3 = Room("The Rockaoke room", 15, 10)
        self.room_4 = Room("The Rapaoke room", 2, 50)

    def test_guest_name(self):
        self.assertEqual("Antonia", self.guest_3.name)

    def test_guest_wallet(self):
        self.assertEqual(100, self.guest_2.wallet) 

    def test_guest_favourite_song(self):
        self.assertEqual("We will rock you", self.guest_4.favourite_song) 

# Extension

    def test_entry_fee_has_been_charged(self):
        self.room_4.charge_entry_fee(self.guest_1)
        self.assertEqual(100, self.guest_1.wallet)

    def test_entry_fee_has_been_charged_2(self):
        self.room_2.charge_entry_fee(self.guest_1)
        self.room_2.charge_entry_fee(self.guest_4)
        self.assertEqual(130, self.guest_1.wallet)
        self.assertEqual(280, self.guest_4.wallet)

    def test_entry_fee_has_been_charged_3(self):
        self.room_4.check_in_guest_to_room(self.guest_1)
        self.room_4.check_in_guest_to_room(self.guest_2)
        self.room_4.check_in_guest_to_room(self.guest_3)
        self.assertEqual(100, self.guest_1.wallet)
        self.assertEqual(50, self.guest_2.wallet)
        self.assertEqual(200, self.guest_3.wallet)
        self.assertEqual(2, len(self.room_4.guests))