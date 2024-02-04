from datetime import date, time

class Event:
    EVENT_TYPES = ['Movie', 'Concert', 'Sports']

    def __init__(self, event_name, event_date, event_time, venue_name, total_seats, ticket_price, event_type):
        self._available_seats = 0
        self._event_name = event_name
        self._event_date = event_date
        self._event_time = event_time
        self._venue_name = venue_name
        self._total_seats = total_seats
        self._ticket_price = ticket_price
        self._event_type = event_type

    def display_event_details(self):
        print(f"Event Type: {self._event_type}")
        print(f"Event Name: {self._event_name}")
        print(f"Event Date: {self._event_date}")
        print(f"Event Time: {self._event_time}")
        print(f"Venue: {self._venue_name}")
        print(f"Total Seats: {self._total_seats}")
        print(f"Ticket Price: ${self._ticket_price}")

    def calculate_total_revenue(self):
        return self._total_seats * self._ticket_price
    def get_booked_no_of_tickets(self):
        return self._total_seats - self._available_seats
    def book_tickets(self, num_tickets):
        if num_tickets <= self._available_seats:
            self._available_seats -= num_tickets
            print(f"Successfully booked {num_tickets} tickets for {self._event_name}")
        else:
            print("Insufficient available seats")
    def cancel_booking(self, num_tickets):
        if num_tickets <= self._total_seats - self._available_seats:
            self._available_seats += num_tickets
            print(f"Successfully canceled booking for {num_tickets} tickets for {self._event_name}")
        else:
            print("Invalid number of tickets to cancel")




event = Event("Movie Night", date(2024, 2, 10), time(18, 30), "Cinema Hall", 100, 10.50, "Movie")
event.display_event_details()
event.book_tickets(5)
event.cancel_booking(2)
print(f"Total Revenue: ${event.calculate_total_revenue()}")
print(f"Total Booked Tickets: {event.get_booked_no_of_tickets()}")


