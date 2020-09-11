import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):

# MVP
    
    def setUp(self):
        self.room_1 = Room("The Popaoke room", 10)
        self.room_2 = Room("The Countryaoke room", 6)
        self.room_3 = Room("The Rockaoke room", 15)
        self.room_4 = Room("The Rapaoke room", 2)

        self.guest_1 = Guest("David", 150, "Jolene")
        self.guest_2 = Guest("Kyle", 100, "Lovers")
        self.guest_3 = Guest("Antonia", 200, "I should be so lucky")
        self.guest_4 = Guest("Ewen", 50, "We will rock you")

        self.song_1 = Song("I should be so lucky", "Kylie Minogue")
        self.song_2 = Song("Jolene", "Dolly Parton")
        self.song_3 = Song("We will rock you", "Queen")
        self.song_4 = Song("Not afraid", "Eminem")
        self.song_5 = Song("Lovers", "Kylie Minogue")


    def test_room_name(self):
        self.assertEqual("The Rockaoke room", self.room_3.name)

    def test_room_max_occupancy(self):
        self.assertEqual(10, self.room_1.max_occupancy)

    def test_check_in_guest_to_room(self):
        self.room_1.check_in_guest_to_room(self.guest_1)
        self.assertEqual(1, len(self.room_1.guests))

    def test_check_out_guest_from_room(self):
        self.room_3.check_in_guest_to_room(self.guest_4)
        self.room_3.check_out_guest_from_room(self.guest_4)
        self.assertEqual(0, len(self.room_3.guests))

    def test_check_out_guest_from_room_with_other_guests_still_in(self):
        self.room_2.check_in_guest_to_room(self.guest_1)
        self.room_2.check_in_guest_to_room(self.guest_2)
        self.room_2.check_in_guest_to_room(self.guest_3)
        self.room_2.check_out_guest_from_room(self.guest_2)
        self.assertEqual(2, len(self.room_2.guests))

    def test_add_song_to_room(self):
        self.room_4.add_song_to_room(self.song_4)
        self.assertEqual(1, len(self.room_4.songs))

    def test_add_multiple_songs_to_room(self):
        self.room_1.add_song_to_room(self.song_1)
        self.room_1.add_song_to_room(self.song_2)
        self.room_1.add_song_to_room(self.song_3)
        self.room_1.add_song_to_room(self.song_5)
        self.assertEqual(4, len(self.room_1.songs))

    def test_removing_song_from_room(self):
        self.room_2.add_song_to_room(self.song_4)
        self.room_2.remove_song_from_room(self.song_4)
        self.assertEqual(0, len(self.room_2.songs))

    def test_removing_song_from_room_with_multiple_songs(self):
        self.room_3.add_song_to_room(self.song_1)
        self.room_3.add_song_to_room(self.song_2)
        self.room_3.add_song_to_room(self.song_3)
        self.room_3.remove_song_from_room(self.song_2)
        self.assertEqual(2, len(self.room_3.songs))

# Extensions

    def test_room_capacity_right_number_of_guests(self):
        self.room_4.check_in_guest_to_room(self.guest_1)
        self.room_4.check_in_guest_to_room(self.guest_2)
        self.assertEqual(2, len(self.room_4.guests))