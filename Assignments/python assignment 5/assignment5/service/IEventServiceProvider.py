from abc import ABC, abstractmethod
from assignment5.venue import Venue
from assignment5.event import Event
from typing import List

class IEventServiceProvider(ABC):

    @abstractmethod
    def create_event(self, event_name: str, date: str, time: str, total_seats: int, ticket_price: float,
                     event_type: str, venue: Venue) -> Event:
        pass

    @abstractmethod
    def get_event_details(self) -> List[str]:
        pass

    @abstractmethod
    def get_available_no_of_tickets(self):
        pass