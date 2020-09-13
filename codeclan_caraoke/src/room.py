class Room:

# MVP

    def __init__(self, input_name, input_max_occupancy, input_fee):
        self.name = input_name
        self.songs = []
        self.max_occupancy = input_max_occupancy
        self.guests = []
        self.fee = input_fee

    def check_in_guest_to_room(self, guest):
        if len(self.guests) < self.max_occupancy: # Refactored for Extension
            self.guests.append(guest)
            self.charge_entry_fee(guest)
        else:
            return "Room is full"

    def check_out_guest_from_room(self, guest):
        self.guests.remove(guest)

    def add_song_to_room(self, song):
        self.songs.append(song)

    def remove_song_from_room(self, song):
        self.songs.remove(song)

# Extensions

    def charge_entry_fee(self, guest):
        guest.wallet -= self.fee