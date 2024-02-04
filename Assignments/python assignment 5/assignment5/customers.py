class Customers:
    def __init__(self, CustomerName, Email, PhoneNumber):
        self._customer_name = CustomerName
        self._email = Email
        self._phone_number = PhoneNumber



    def display_customer_details(self):
        print(f"Customer Name: {self._customer_name}")
        print(f"Email: {self._email}")
        print(f"Phone Number: {self._phone_number}")