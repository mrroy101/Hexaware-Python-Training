from typing import List
from datetime import date, time
from assignment5.event import Event
from assignment5.venue import Venue
from assignment5.service.IEventServiceProvider import IEventServiceProvider

class EventServiceProviderImpl(IEventServiceProvider):

    def __init__(self):
        self.events = []

    def create_event(self, event_name: str, date_str: str, time_str: str, total_seats: int, ticket_price: float,
                     event_type: str, venue: Venue) -> Event:
        event_date = date(*map(int, date_str.split('-')))
        event_time = time(*map(int, time_str.split(':')))
        event = Event(event_name, event_date, event_time, venue, total_seats, ticket_price, event_type)
        self.events.append(event)
        return event

    def get_event_details(self) -> List[str]:
        event_details = [event.event_name for event in self.events]
        return event_details

    def get_available_no_of_tickets(self) -> int:
        if not self.events:
            return 0
        return self.events[0].available_seats