class Event:
    EVENT_TYPES = ('Movie', 'Sports', 'Concert')

class Venue:
    def __init__(self, Venueame, Address):
        self._venue_name = Venueame
        self._address = Address


    def display_venue_details(self):
        print(f"Venue Name: {self._venue_name}")
        print(f"Address: {self._address}")
