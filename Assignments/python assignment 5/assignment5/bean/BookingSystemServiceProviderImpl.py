from typing import List
from assignment5.booking import Booking
from assignment5.customers import Customers
from assignment5.bean.EventServiceProviderImpl import EventServiceProviderImpl
from assignment5.service.IBookingSystemServiceProvider import IBookingSystemServiceProvider


class BookingSystemServiceProviderImpl(EventServiceProviderImpl, IBookingSystemServiceProvider):

    def __init__(self):
        super().__init__()

    def calculate_booking_cost(self, num_tickets: int) -> float:
        if num_tickets > 0:
            return num_tickets * self.selected_event.ticket_price
        else:
            print("Invalid number of tickets.")
            return 0.0

    def book_tickets(self, event_name: str, num_tickets: int, array_of_customers: List[Customers]) -> None:
        global booking
        self.selected_event = None

        for event in self.events:
            if event.event_name == event_name:
                self.selected_event = event
                break

            if self.selected_event is not None:
                for _ in range(num_tickets):
                    customer_name = input("Enter customer name: ")
                    customer = Customers(customer_name )
                    array_of_customers.append(customer)

                total_cost = self.calculate_booking_cost(num_tickets)
                booking = Booking(array_of_customers, self.selected_event, num_tickets)
                booking.total_cost = total_cost
            booking.display_booking_details()
        else:
            print(f"\nEvent with name '{event_name}' not found.")

    def cancel_booking(self, booking_id: int) -> None:
        for event in self.events:
            for booking in event.bookings:
                if booking.booking_id == booking_id:
                    event.available_seats += booking.num_tickets
                    event.bookings.remove(booking)
                    print("\nBooking with ID {} canceled successfully.".format(booking_id))
                    return
        print("\nBooking with ID {} not found.".format(booking_id))

    def get_booking_details(self, booking_id: int) -> None:
        for event in self.events:
            for booking in event.bookings:
                if booking.booking_id == booking_id:
                    print("\nBooking Details:")
                    booking.display_booking_details()
                    return
        print("\nBooking with ID {} not found.".format(booking_id))