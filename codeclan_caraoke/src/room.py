class Room:

# MVP

    def __init__(self, input_name, input_max_occupancy):
        self.name = input_name
        self.songs = []
        self.max_occupancy = input_max_occupancy
        self.guests = []

    def check_in_guest_to_room(self, guest):
        self.guests.append(guest)

    def check_out_guest_from_room(self, guest):
        self.guests.remove(guest)

    def add_song_to_room(self, song):
        self.songs.append(song)

    def remove_song_from_room(self, song):
        self.songs.remove(song)