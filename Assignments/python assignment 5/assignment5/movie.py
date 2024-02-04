from datetime import date, time
from assignment5.event import Event

class Movie(Event):
    def __init__(self, event_name, event_date, event_time,
                 venue_name, total_seats, ticket_price, event_type,
                 genre, actor_name, actress_name):
        super().__init__(event_name, event_date, event_time,
                         venue_name, total_seats, ticket_price, event_type)
        self._genre = genre
        self._actor_name = actor_name
        self._actress_name = actress_name


    def display_event_details(self):
        super().display_event_details()
        print(f"Genre: {self._genre}")
        print(f"Actor: {self._actor_name}")
        print(f"Actress: {self._actress_name}")


if __name__ == "__main__":
    movie = Movie("Movie Night", date(2024, 2, 10), time(18, 30), "PVR", 100, 10.50, "Movie", "Action", "Hritik Roshan", "Katrina Kaif")
    #movie.display_event_details()