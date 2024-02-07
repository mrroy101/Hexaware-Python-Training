from Entity.Customer import Customer
from Entity.Product import Product
from dao.OrderProcessorRepositoryImpl import OrderProcessorRepositoryImpl


class MainModule():
    def __init__(self):
        self.service = OrderProcessorRepositoryImpl()

    @staticmethod
    def main():
        main_module = MainModule()  # Create an instance of MainModule
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
                value = main_module.service.create_customer(Customer)
                if value is True:
                    print("succesfully added customer")


            elif choice == '2':
                value = main_module.service.create_product(Product)
                if value is True:
                    print("succesfully added product")


            elif choice == '3':
                id = input(print("enter the product id to delete : "))
                value = main_module.service.delete_product(id)
                if value is True:
                    print(f'succesfully deleted the product with product id {id}')


            elif choice =='4':
                id = input(print("enter the customer id to delete : "))
                value = main_module.service.delete_customer(id)
                if value is True:
                    print(f'succesfully deleted the customer with customer id {id}')


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
