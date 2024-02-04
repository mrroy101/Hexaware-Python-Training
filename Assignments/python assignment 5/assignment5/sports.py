from datetime import date, time
from assignment5.event import Event

class Sports(Event):
    def __init__(self, event_name, event_date, event_time,
                 venue_name, total_seats, ticket_price,
                 event_type, sport_name, teams_name):
        super().__init__(event_name, event_date,
                         event_time, venue_name, total_seats,
                         ticket_price, event_type)
        self._sport_name = sport_name
        self._teams_name = teams_name


    def display_sport_details(self):
        super().display_event_details()
        print(f"Sport Name: {self._sport_name}")
        print(f"Teams Name: {self._teams_name}")


if __name__ == "__main__":
    sports_event = Sports("Cricket Match", date(2024, 3, 1), time(14, 30), "Stadium", 500, 1500.0, "Sports", "Cricket", "India vs Pakistan")
    sports_event.display_sport_details()
