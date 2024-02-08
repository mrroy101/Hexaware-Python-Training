from Entity.Customer import Customer
from Entity.Product import Product
from dao.OrderProcessorRepositoryImpl import OrderProcessorRepositoryImpl


class MainModule():
    def __init__(self):
        self.service = OrderProcessorRepositoryImpl()

    @staticmethod
    def main():
        main_module = MainModule()  # Create an instance of MainModule
        password = 'admin@123'
        while True:
            print("\n1. Register Customer")
            print("2. Create Product")
            print("3. Delete Product")
            print("4. Delete Customer")
            print("5. Add to Cart")
            print("6. Remove from Cart")
            print("7. View Cart")
            print("8. Place Order")
            print("9. View Customer Order")
            print("0. Exit the Program")


            choice = input("Enter your choice: ")

            if choice == '1':
                p1 = input("Enter the password to get access: ")
                if p1 == password:
                    value = main_module.service.create_customer(Customer)
                    if value is True:
                        print("Successfully added customer")
                else:
                    print("Incorrect password. Access denied.")


            elif choice == '2':
                p1 = input("Enter the password to get access: ")
                if p1 == password:
                    value = main_module.service.create_product(Product)
                    if value is True:
                        print("succesfully added product")
                else:
                    print("Incorrect password. Access denied.")


            elif choice == '3':
                p1 = input("Enter the password to get access: ")
                if p1 == password:
                    product_id = int(input("Enter the product ID to delete: "))
                    value = main_module.service.delete_product(product_id)
                    if value is True:
                        print("Successfully deleted product")
                else:
                    print("Incorrect password. Access denied.")



            elif choice =='4':
                p1 = input("Enter the password to get access: ")
                if p1 == password:
                    customer_id = input("enter the customer id to delete : ")
                    value = main_module.service.delete_customer(customer_id)
                    if value is True:
                        print(f'succesfully deleted the customer with customer id {customer_id}')
                else:
                    print("Incorrect password. Access denied.")


            elif choice == '5':
                value = main_module.service.add_to_cart(Customer , Product , quantity=None)
                if value is True:
                    print(f'succesfully added to cart')


            elif choice == '6':
                value = main_module.service.remove_from_cart(Customer , Product)
                if value is True:
                    print(f'succesfully removed from cart')


            elif choice == '7':
                cart_products  = main_module.service.get_all_from_cart(Customer)
                if cart_products:
                    print("Products in the cart:")
                    for product in cart_products:
                        print("Product ID:", product.get_product_id())
                        print("Name:", product.get_name())
                        print("Price:", product.get_price())
                        print("Description:", product.get_description())
                        print("Stock Quantity:", product.get_stock_quantity())
                        print("-------------------------")
                else:
                    print("No products found in the cart.")


            elif choice == '8':
                value = main_module.service.place_order(Customer , products_quantities = 0)
                if value is True :
                    print("order succesfully placed")


            elif choice == '9':
                id = input(print("enter the customer id  : "))
                orders = main_module.service.get_orders_by_customer(id)
                print("Orders for customer ID", id, ":")
                for order in orders:
                    for product, quantity in order.items():
                        print("Product:", product.get_name(), ", Quantity:", quantity)


            elif choice == '0':
                print("exiting the program ")
                break


            else :
                print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    MainModule.main()
