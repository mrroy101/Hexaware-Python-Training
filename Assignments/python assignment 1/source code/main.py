import techshopIMPL


class Main:
    def start(self):
        while True:
            print("Please select the choices from below:")
            print("1. Register new customer.")
            print("2. Change product information.")
            print("3. Tracking Order Status")
            print("4. Inventory Management")
            print("5. Sales Reporting")
            print("6. Customer Account Updates")
            print("7. Payment Processing")
            print("8. Product Search and Recommendations")
            print("0. Exit")
            choice = int(input("Enter your choice: "))

            match choice :
                case 1:
                    techshopIMPL.customer_registration()
                case 2:
                    techshopIMPL.update_product()
                case 3:
                    techshopIMPL.order_tracking()
                case 4:
                    techshopIMPL.inventory_management()
                case 5:
                    techshopIMPL.sales_report()
                case 6:
                    techshopIMPL.customer_account_updates()
                case 7:
                    techshopIMPL.payment_processing()
                case 8:
                    techshopIMPL.product_search_and_recommendations()
                case 0:
                    break



m1 = Main()
m1.start()


