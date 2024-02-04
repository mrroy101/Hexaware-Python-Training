import event
from assignment5.movie import Movie
from assignment5.concert import Concert
from assignment5.sports import Sports

class TicketBookingSystem:
    def create_event(self, event_name, event_date, event_time,
                     total_seats, ticket_price, event_type, venue_name):
        event_type = event_type.capitalize()

        if event_type in event.EVENT_TYPES:
            if event_type == 'Movie':
                genre = input("Enter movie genre: ")
                actor_name = input("Enter actor name: ")
                actress_name = input("Enter actress name: ")
                return Movie(event_name, event_date, event_time, venue_name, total_seats, ticket_price, event_type,
                             genre, actor_name, actress_name)
            elif event_type == 'Concert':
                artist = input("Enter artist/band name: ")
                concert_type = input("Enter concert type: ")
                return Concert(event_name, event_date, event_time, venue_name, total_seats, ticket_price,
                               event_type, artist, concert_type)
            elif event_type == 'Sports':
                sport_name = input("Enter sport name: ")
                teams_name = input("Enter teams names: ")
                return Sports(event_name, event_date, event_time, venue_name, total_seats, ticket_price, event_type,
                              sport_name, teams_name)
        else:
            raise ValueError("Invalid event type. Please enter 'Movie', 'Sports', or 'Concert'.")

    def display_event_details(self, event):
        event.display_event_details()

    def book_tickets(self, event, num_tickets):
        return event.book_tickets(num_tickets)

    def cancel_tickets(self, event, num_tickets):
        event.cancel_booking(num_tickets)

    def main(self):
        print("Welcome to the Ticket Booking System!")

        while True:
            print("\nMenu:")
            print("1. Create Event")
            print("2. Display Event Details")
            print("3. Book Tickets")
            print("4. Cancel Tickets")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                event_name = input("Enter event name: ")
                event_date = input("Enter event date (YYYY-MM-DD): ")
                event_time = input("Enter event time (HH:MM): ")
                total_seats = int(input("Enter total seats: "))
                ticket_price = float(input("Enter ticket price: "))
                event_type = input("Enter event type (Movie/Sports/Concert): ")
                venue_name = input("Enter venue name: ")

                event = self.create_event(event_name, event_date, event_time, total_seats, ticket_price, event_type,
                                          venue_name)
                print(f"Event '{event_name}' created successfully!")

            elif choice == '2':
                event_type = input("Enter event type (Movie/Sports/Concert): ")
                if event_type in event.EVENT_TYPES:
                    event_name = input("Enter event name: ")
                    event_date = input("Enter event date (YYYY-MM-DD): ")
                    event_time = input("Enter event time (HH:MM): ")

                    events = self.create_event(event_name, event_date, event_time, 0, 0.0, event_type, "")
                    self.display_event_details(events)
                else:
                    print("Invalid event type")

            elif choice == '3':
                event_type = input("Enter event type (Movie/Sports/Concert): ")

                if event_type in event.EVENT_TYPES:
                    event_name = input("Enter event name: ")
                    event_date = input("Enter event date (YYYY-MM-DD): ")
                    event_time = input("Enter event time (HH:MM): ")

                    events = self.create_event(event_name, event_date, event_time, 0, 0.0, event_type, "")
                    num_tickets = int(input("Enter the number of tickets to book: "))
                    total_cost = self.book_tickets(events, num_tickets)
                    print(f"Total cost of booking: ${total_cost}")
                else:
                    print("Invalid event type")

            elif choice == '4':
                event_type = input("Enter event type (Movie/Sports/Concert): ")
                if event_type in event.EVENT_TYPES:
                    event_name = input("Enter event name: ")
                    event_date = input("Enter event date (YYYY-MM-DD): ")
                    event_time = input("Enter event time (HH:MM): ")

                    events = self.create_event(event_name, event_date, event_time, 0, 0.0, event_type, "")
                    num_tickets = int(input("Enter the number of tickets to cancel: "))
                    self.cancel_tickets(events, num_tickets)
                    print(f"Booking for {num_tickets} tickets canceled successfully!")
                else:
                    print("Invalid event type")

            elif choice == '5':
                print("Thank you for using the Ticket Booking System!")
                break

            else:
                print("Invalid choice. Please enter a valid option (1-5).")


if __name__ == "__main__":
    ticket_booking_system = TicketBookingSystem()
    ticket_booking_system.main()