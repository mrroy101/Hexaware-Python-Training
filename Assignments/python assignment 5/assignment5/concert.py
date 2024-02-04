from datetime import date, time
from assignment5.event import Event

class Concert(Event):
    def __init__(self, event_name, event_date, event_time,
                 venue_name, total_seats, ticket_price,
                 event_type, artist, concert_type):
        super().__init__(event_name, event_date,
                         event_time, venue_name, total_seats,
                         ticket_price, event_type)
        self._artist = artist
        self._concert_type = concert_type


    def display_concert_details(self):
        super().display_event_details()
        print(f"Artist: {self._artist}")
        print(f"Concert Type: {self._concert_type}")
if __name__ == "__main__":
    concert = Concert("Concert Night", date(2024, 2, 15), time(20, 0), "Concert Hall", 200, 25000.0, "Concert", "Bangtan Sonyeodan BTS", "kpop")
    concert.display_concert_details()
