from assignment5.bean.BookingSystemServiceProviderImpl import BookingSystemServiceProviderImpl



class TicketBookingSystem:

    def __init__(self):
        self.booking_system_provider = BookingSystemServiceProviderImpl()

    def display_menu(self):
        print("\n===== Ticket Booking System Menu =====")
        print("1. Create Event")
        print("2. Get Event Details")
        print("3. Book Tickets")
        print("4. Cancel Booking")
        print("5. Get Available Seats")
        print("6. Exit")

    def main(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                self.create_event()
            elif choice == "2":
                self.get_event_details()
            elif choice == "3":
                self.book_tickets()
            elif choice == "4":
                self.cancel_booking()
            elif choice == "5":
                self.get_available_seats()
            elif choice == "6":
                print("Exiting the Ticket Booking System.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def create_event(self):
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
    def get_event_details(self):
        event_details = self.booking_system_provider.get_event_details()
        print("Event Details:")
        for detail in event_details:
            print(detail)

    def book_tickets(self):
        event_name = input("Enter the name of the event to book tickets: ")
        num_tickets = int(input("Enter the number of tickets to book: "))
        array_of_customer_names = []

        for _ in range(num_tickets):
            customer_name = input("Enter customer name: ")
            array_of_customer_names.append(customer_name)
        self.booking_system_provider.book_tickets(event_name, num_tickets, array_of_customer_names)
        print("Booking successful!")

    def cancel_booking(self):
        customer_name = input("Enter the customer name to cancel the booking: ")
        self.booking_system_provider.cancel_booking(customer_name)
        print("Booking canceled successfully!")
    def get_available_seats(self):
        available_seats = self.booking_system_provider.get_available_no_of_tickets()
        print(f"Available Seats: {available_seats}")


if __name__ == "__main__":
    ticket_booking_system = TicketBookingSystem()
    ticket_booking_system.main()
