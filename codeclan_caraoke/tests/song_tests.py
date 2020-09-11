import unittest
from src.song import Song

class TestSong(unittest.TestCase):

# MVP
    
    def setUp(self):
        self.song_1 = Song("I should be so lucky", "Kylie Minogue")
        self.song_2 = Song("Jolene", "Dolly Parton")
        self.song_3 = Song("We will rock you", "Queen")
        self.song_4 = Song("Not afraid", "Eminem")
        self.song_5 = Song("Lovers", "Kylie Minogue")

    def test_song_name(self):
        self.assertEqual("Jolene", self.song_2.name)

    def test_song_artist(self):
        self.assertEqual("Eminem", self.song_4.artist)

