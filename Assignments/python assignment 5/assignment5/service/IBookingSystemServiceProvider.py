from abc import ABC, abstractmethod
from assignment5.customers import Customers
from typing import List
class IBookingSystemServiceProvider(ABC):

    @abstractmethod
    def calculate_booking_cost(self, num_tickets: int) -> float:
        pass

    @abstractmethod
    def book_tickets(self, event_name: str, num_tickets: int, array_of_customers: List[Customers]) -> None:
        pass

    @abstractmethod
    def cancel_booking(self, booking_id: int) -> None:
        pass

    @abstractmethod
    def get_booking_details(self, booking_id: int) -> None:
        pass