import mysql.connector
import re

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    port="3306",
    database="TechShopDB"
)

cur = con.cursor()
cur.execute("use TechShopDB")

def customer_registration():
    id = int(input("Enter customer id: "))
    firstname = input("Enter first name: ")
    lastname = input("Enter last name: ")
    email = input("Enter email: ")
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.match(pat, email):
        print("Valid Email")
    else:
        raise Exception("Invalid Email")
    phone = input("Enter phone: ")
    address = input("Enter address: ")
    str1 = "insert into Customers values(%s,%s,%s,%s,%s,%s)"
    cur.execute(str1, (id, firstname, lastname, email, phone, address))
    con.commit()
    print("User registered successfully")


def update_product():
    print("Select 1 for product name update\n"
          "Select 2 for product description update\n"
          "Select 3 for price update\n")

    select = int(input("Enter choice: "))

    if select not in [1, 2, 3]:
        print("Invalid choice")
        return

    prodid = int(input("Enter product id: "))

    if select == 1:
        prodname = input("Enter new product name: ")
        query = "UPDATE products SET productname = %s WHERE productID = %s"
        cur.execute(query, (prodname, prodid))

    elif select == 2:
        desc = input("Enter new product description: ")
        query = "UPDATE products SET description = %s WHERE productID = %s"
        cur.execute(query, (desc, prodid))

    elif select == 3:
        price = float(input("Enter new product price: "))
        query = "UPDATE products SET price = %s WHERE productID = %s"
        cur.execute(query, (price, prodid))

    con.commit()
    print("Product successfully updated")


def order_tracking():
    id = int(input("Enter customer id: "))

    # Use a parameterized query to avoid SQL injection
    query = "SELECT orderID FROM orders WHERE customerID = %s AND orderdate > '2024-01-15'"
    cur.execute(query, (id,))

    orders = cur.fetchall()

    if not orders:
        raise Exception("No orders found for the customer.")
        return

    for order in orders:
        order_id = order[0]
        print(f"Order ID: {order_id}, Status: {'shipped' if order[1] > '2024-01-15' else 'pending'}")


def inventory_management():
    print("1. Add New Product")
    print("2. Update Product Quantity")
    print("3. Discontinue Product")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_new_product()
    elif choice == 2:
        update_product_quantity()
    elif choice == 3:
        discontinue_product()
    else:
        print("Invalid choice")

def add_new_product():
    name = input("Enter product name: ")
    description = input("Enter product description: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))

    # Insert new product into the Products table
    query = "INSERT INTO Products (ProductName, Description, Price) VALUES (%s, %s, %s)"
    cur.execute(query, (name, description, price))
    con.commit()

    # Add the product to the Inventory
    product_id = cur.lastrowid
    query_inventory = "INSERT INTO Inventory (ProductID, QuantityInStock) VALUES (%s, %s)"
    cur.execute(query_inventory, (product_id, quantity))
    con.commit()

    print("New product added successfully.")

def update_product_quantity():
    product_id = int(input("Enter product ID: "))
    new_quantity = int(input("Enter new product quantity: "))

    # Update product quantity in the Inventory
    query = "UPDATE Inventory SET QuantityInStock = %s WHERE ProductID = %s"
    cur.execute(query, (new_quantity, product_id))
    con.commit()

    print("Product quantity updated successfully.")

def discontinue_product():
    product_id = int(input("Enter product ID to discontinue: "))

    # Mark the product as discontinued in the Products table
    query_product = "UPDATE Products SET Discontinued = 1 WHERE ProductID = %s"
    cur.execute(query_product, (product_id,))
    con.commit()

    # Remove the product from the Inventory
    query_inventory = "DELETE FROM Inventory WHERE ProductID = %s"
    cur.execute(query_inventory, (product_id,))
    con.commit()

    print("Product discontinued successfully.")


def sales_report():
    # Fetch relevant data from the database
    cur.execute("SELECT od.OrderID, p.ProductName, od.Quantity, p.Price, od.Quantity * p.Price AS TotalAmount "
                "FROM orderdetails od "
                "JOIN products p ON od.ProductID = p.ProductID")

    # Display the sales report
    print("\nSales Report:")
    print("{:<10} {:<20} {:<10} {:<10} {:<10}".format("OrderID", "Product Name", "Quantity", "Price", "Total Amount"))
    print("-" * 60)

    for row in cur:
        order_id, product_name, quantity, price, total_amount = row
        print("{:<10} {:<20} {:<10} {:<10} {:<10}".format(order_id, product_name, quantity, price, total_amount))

    print("\nSales Report generated successfully.")

def customer_account_updates():
    customer_id = int(input("Enter customer ID: "))
    print("Select the information to update:")
    print("1. Email")
    print("2. Phone")
    choice = int(input("Enter your choice: "))

    if choice not in [1, 2]:
        print("Invalid choice")
        return

    if choice == 1:
        new_email = input("Enter new email: ")
        validate_email(new_email)
        query = "UPDATE Customers SET Email = %s WHERE CustomerID = %s"
        cur.execute(query, (new_email, customer_id))
    elif choice == 2:
        new_phone = input("Enter new phone number: ")
        query = "UPDATE Customers SET Phone = %s WHERE CustomerID = %s"
        cur.execute(query, (new_phone, customer_id))

    con.commit()
    print("Customer information updated successfully.")

def payment_processing():
    order_id = int(input("Enter order ID: "))
    payment_method = input("Enter payment method: ")
    amount = float(input("Enter payment amount: "))

    # Record payment details in the Payments table
    query_payment = "INSERT INTO Payments (OrderID, PaymentMethod, Amount) VALUES (%s, %s, %s)"
    cur.execute(query_payment, (order_id, payment_method, amount))
    con.commit()

    print("Payment processed successfully.")

def product_search_and_recommendations():
    print("Select the search criteria:")
    print("1. Search by product name")
    print("2. Search by category")
    choice = int(input("Enter your choice: "))

    if choice not in [1, 2]:
        print("Invalid choice")
        return

    if choice == 1:
        product_name = input("Enter product name to search: ")
        query = "SELECT * FROM Products WHERE ProductName LIKE %s"
        cur.execute(query, ('%' + product_name + '%',))
    elif choice == 2:
        category = input("Enter category to search: ")
        query = "SELECT * FROM Products WHERE Category = %s"
        cur.execute(query, (category,))

    products = cur.fetchall()

    if not products:
        print("No products found.")
    else:
        print("\nSearch Results:")
        for product in products:
            print(product)

def validate_email(email):
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if not re.match(pat, email):
        raise Exception("Invalid Email")

