def book_tickets(available_tickets, no_of_booking_tickets):
    if available_tickets >= no_of_booking_tickets:
        remaining_tickets = available_tickets - no_of_booking_tickets
        print(f"Tickets booked successfully! Remaining tickets: {remaining_tickets}")
    else:
        print("Sorry, not enough tickets available.")

available_tickets = int(input("Enter the number of available tickets: "))
no_of_booking_tickets = int(input("Enter the number of tickets to book: "))

# Checking availability and displaying messages
book_tickets(available_tickets, no_of_booking_tickets)

def calculate_ticket_cost(category, no_of_tickets):
    base_prices = {"Silver": 50, "Gold": 100, "Diamond": 200}

    if category in base_prices:
        base_price = base_prices[category]
        total_cost = base_price * no_of_tickets
        print(f"Total cost for {no_of_tickets} {category} tickets: ${total_cost}")
    else:
        print("Invalid ticket category.")

# Taking input
ticket_category = input("Enter the ticket category (Silver/Gold/Diamond): ")
no_of_tickets = int(input("Enter the number of tickets you want to book: "))

# Calculating and displaying total cost
calculate_ticket_cost(ticket_category, no_of_tickets)

while True:
    # Taking input for Task 2
    ticket_category = input("Enter the ticket category (Silver/Gold/Diamond) or type 'Exit' to end: ")

    # Check if the user wants to exit
    if ticket_category.lower() == 'exit':
        print("Exiting the booking system.")
        break

    no_of_tickets = int(input("Enter the number of tickets you want to book: "))

    # Calculate and display total cost
    calculate_ticket_cost(ticket_category, no_of_tickets)
