from OrderManagement.Product import Product
from OrderManagement.dao.OrderProcessor import OrderProcessor
from OrderManagement.User import User
class MainModule(OrderProcessor):


    def display_menu(self):
        print("Menu:")
        print("1. Create User")
        print("2. Create Product")
        print("3. Create Order")
        print("4. Cancel Order")
        print("5. Get All Products")
        print("6. Get Order by User")
        print("7. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                self.OrderProcessor.create_user(User)
            elif choice =="2":
                self.createUser(User)
            elif choice == "3":
                userID = int(input("enter the userID : "))
                orderID = int(input("enter the order id : "))
                self.OrderProcessor.cancelOrder(orderID,userID)
            elif choice =="4":
                self.createProduct(User , Product)
            elif choice =="5":
                self.getAllProducts()
            elif choice =="6":
                self.getOrderByUser(User)
            elif choice == "7":
                print("exiting from menu" )
                break
            else :
                print("enter correct choice")






if __name__ == "__main__":
    main_module = MainModule()
    main_module.run()