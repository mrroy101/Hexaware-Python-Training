from assignment5.bean.BookingSystemServiceProviderImpl import BookingSystemServiceProviderImpl

class EventNotFoundException(Exception):
    pass

class InvalidBookingIDException(Exception):
    pass

class CustomNullPointerException(Exception):
    pass

class TicketBookingExceptionHandler:

    def handle_event_not_found(self, event_name):
        raise EventNotFoundException(f"Event '{event_name}' not found in the menu.")

    def handle_invalid_booking_id(self):
        raise InvalidBookingIDException("Invalid Booking ID.")

    def handle_null_pointer(self):
        raise CustomNullPointerException("Null Pointer Exception.")

class TicketBookingSystem:

    def __init__(self):
        self.booking_system_provider = BookingSystemServiceProviderImpl()
        self.exception_handler = TicketBookingExceptionHandler()

    def display_menu(self):
        print("\n===== Ticket Booking System Menu =====")
        print("1. Create Event")
        print("2. Get Event Details")
        print("3. Book Tickets")
        print("4. Cancel Booking")
        print("5. Get Available Seats")
        print("6. Exit")

    def create_event(self):
        try:
                event_name = input("Enter event name: ")
                date = input("Enter event date (YYYY-MM-DD): ")
                time = input("Enter event time (HH:MM): ")
                total_seats = int(input("Enter total seats: "))
                ticket_price = float(input("Enter ticket price: "))
                event_type = input("Enter event type (Movie/Concert/Sports): ")
                venue_name = input("Enter venue name: ")

                self.booking_system_provider.create_event(event_name, date, time, total_seats, ticket_price, event_type,
                                                          venue_name)
                print("Event created successfully!")
        except Exception as e:
            print(f"Error: {e}")
            self.exception_handler.handle_null_pointer()

    def get_event_details(self):
        try:
            event_details = self.booking_system_provider.get_event_details()
            print("Event Details:")
            for detail in event_details:
                print(detail)
        except Exception as e:
            print(f"Error: {e}")
            self.exception_handler.handle_null_pointer()

    def book_tickets(self):
        try:
            event_name = input("Enter the name of the event to book tickets: ")
            num_tickets = int(input("Enter the number of tickets to book: "))
            array_of_customers = []

            self.booking_system_provider.book_tickets(event_name, num_tickets, array_of_customers)
            print("Booking successful!")
        except EventNotFoundException as e:
            print(f"Error: {e}")
            self.exception_handler.handle_event_not_found(event_name)
        except InvalidBookingIDException as e:
            print(f"Error: {e}")
            self.exception_handler.handle_invalid_booking_id()
        except Exception as e:
            print(f"Error: {e}")
            self.exception_handler.handle_null_pointer()

    def cancel_booking(self):
        try:
            customer_name = input("Enter the customer name to cancel the booking: ")
            self.booking_system_provider.cancel_booking(customer_name)
            print("Booking canceled successfully!")
        except InvalidBookingIDException as e:
            print(f"Error: {e}")
            self.exception_handler.handle_invalid_booking_id()
        except Exception as e:
            print(f"Error: {e}")
            self.exception_handler.handle_null_pointer()

    def get_available_seats(self):
        try:
            available_seats = self.booking_system_provider.get_available_no_of_tickets()
            print(f"Available Seats: {available_seats}")
        except Exception as e:
            print(f"Error: {e}")
            self.exception_handler.handle_null_pointer()

