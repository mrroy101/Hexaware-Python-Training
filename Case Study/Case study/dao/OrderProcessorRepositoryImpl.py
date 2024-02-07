from typing import List, Dict

from Entity.Cart import Cart
from Entity.Customer import Customer
from Entity.Product import Product
from dao.OrderProcessorRepository import OrderProcessorRepository
from myExceptions.myExceptions import OrderNotFoundException, CustomerNotFoundException, ProductNotFoundException
from util.DBUtil import DBConnection


class OrderProcessorRepositoryImpl(OrderProcessorRepository):
    def __init__(self):
        self.connection = DBConnection.get_connection()

    def create_product(self, product: Product) -> bool:
        try:
            cursor = self.connection.cursor()
            cursor.execute("USE Ecommerce")

            print("Enter the product details:")
            name = input("Name: ")
            price = input("Price: ")
            description = input("Description: ")
            stock_quantity = input("Stock Quantity: ")

            product = Product(product_id="", name=name, price=price, description=description,
                              stock_quantity=stock_quantity)
            print(product.get_name())

            query = "INSERT INTO products (product_name, price, description, stockQuantity) VALUES (%s, %s, %s, %s)"
            values = (product.get_name(), product.get_price(), product.get_description(), product.get_stock_quantity())

            # Execute the SQL query
            cursor.execute(query, values)

            # Commit the transaction
            self.connection.commit()

            # Close cursor and return True indicating successful insertion
            cursor.close()
            return True
        except Exception as err:
            print("Error while creating product:", err)
            return False



    def create_customer(self, customer: Customer) -> bool:
        try:
            cursor = self.connection.cursor()
            cursor.execute("USE Ecommerce")

            print("Enter the customer details:")
            name = input("Name: ")
            email = input("Email: ")
            password = input("Password: ")

            customer = Customer(name=name, email=email, password=password)

            query = "INSERT INTO customers (name, email, password) VALUES (%s, %s, %s)"
            values = (customer.get_name(), customer.get_email(), customer.get_password())

            # Execute the SQL query
            cursor.execute(query, values)

            # Commit the transaction
            self.connection.commit()

            # Close cursor and return True indicating successful insertion
            cursor.close()
            return True
        except Exception as err:
            print("Error while creating customer:", err)
            return False



    def delete_product(self, product_id: int) -> bool:
        try:
            cursor = self.connection.cursor()
            cursor.execute("USE Ecommerce")

            # Construct the SQL query to delete the product
            query = "DELETE FROM products WHERE product_id = %s"

            # Execute the SQL query with the provided product_id
            cursor.execute(query, (product_id,))

            if cursor.rowcount == 0:
                raise ProductNotFoundException(f"Product with ID {product_id} not found")
            # Commit the transaction
            self.connection.commit()

            # Close cursor and return True indicating successful deletion
            cursor.close()
            return True
        except Exception as err:
            print("Error while deleting product:", err)
            return False



    def delete_customer(self, customer_id: int) -> bool:
        try:
            cursor = self.connection.cursor()
            cursor.execute("USE Ecommerce")

            # Prompt user for confirmation


            # Construct the SQL query to delete the customer
            query = "DELETE FROM customers WHERE customer_id = %s"
            values = (customer_id,)

            # Execute the SQL query
            cursor.execute(query, values)

            if cursor.rowcount == 0:
                raise CustomerNotFoundException(f"Customer with ID {customer_id} not found")
            # Commit the transaction
            self.connection.commit()

            # Close cursor and return True indicating successful deletion
            cursor.close()
            print(f"Customer with ID {customer_id} has been successfully deleted.")
            return True
        except Exception as err:
            print("Error while deleting customer:", err)
            return False



    def add_to_cart(self, customer: Customer, product: Product, quantity: int) -> bool:
        try:
            cursor = self.connection.cursor()
            cursor.execute("USE Ecommerce")

            print("Enter the product details:")
            customerID = input("customer id : ")
            productID = input("product id: ")
            quantity = input("quantity : ")

            cart = Cart(customer_id=customerID, product_id=productID, quantity=quantity)

            query = "INSERT INTO cart (customer_id, product_id, quantity) VALUES (%s, %s, %s)"
            values = (cart.get_customer_id(), cart.get_product_id(), cart.get_quantity())

            # Execute the SQL query
            cursor.execute(query, values)

            # Commit the transaction
            self.connection.commit()

            # Close cursor and return True indicating successful insertion
            cursor.close()
            return True
        except Exception as err:
            print("Error while adding to cart:", err)
            return False

    def remove_from_cart(self, customer: Customer, product: Product) -> bool:
        try:
            cursor = self.connection.cursor()
            cursor.execute("USE Ecommerce")

            print("Enter the product details to remove from cart :")
            customerID = input("customer id : ")
            productID = input("product id: ")


            cart = Cart(customer_id=customerID, product_id=productID)

            query = "DELETE FROM cart WHERE customer_id = %s AND product_id = %s"
            values = (cart.get_customer_id(), cart.get_product_id())

            # Execute the SQL query
            cursor.execute(query, values)

            # Commit the transaction
            self.connection.commit()

            # Close cursor and return True indicating successful insertion
            cursor.close()
            return True
        except Exception as err:
            print("Error while adding to cart:", err)
            return False

    def get_all_from_cart(self, customer: Customer) -> List[Product]:
        try:
            cursor = self.connection.cursor()
            cursor.execute("USE Ecommerce")
            print("enter the customer id : ")
            customerID = input("customer id :")
            customer = Customer(customer_id=customerID)

            # Fetch products in the cart for the given customer
            query = "SELECT p.product_id, p.product_name, p.price, p.description, p.stockQuantity " \
                    "FROM cart c " \
                    "JOIN products p ON c.product_id = p.product_id " \
                    "WHERE c.customer_id = %s"
            cursor.execute(query, (customer.get_customer_id(),))

            cart_products = cursor.fetchall()

            products = []
            for row in cart_products:
                product_id, name, price, description, stock_quantity = row
                product = Product(product_id=product_id, name=name, price=price, description=description,
                                  stock_quantity=stock_quantity)
                products.append(product)

            cursor.close()
            return products
        except Exception as err:
            print("Error while fetching products from cart:", err)
            return []



    def place_order(self, customer: Customer, products_quantities: List[Dict[Product, int]]) -> bool:
        try:
            cursor = self.connection.cursor()
            cursor.execute("USE Ecommerce")

            # Prompt the user to enter shipping address
            shipping_address = input("Enter shipping address: ")

            # Get the customer ID
            customerId = input("enter customer id : ")
            productID = input("enter product id :")
            quantity = int(input("enter quantity : "))


            customer = Customer(customer_id = customerId)
            product = Product(product_id=productID)
            val = cursor.execute("select price from products where Product_id = (%s) ",productID)
            total = val * quantity


            # Insert order into orders table
            order_query = ("INSERT INTO orders (customer_id, order_date, total_price, shipping_address)"
                           " VALUES (%s, NOW(), %s , %s)")
            order_values = (customer.get_customer_id(), total , shipping_address)
            cursor.execute(order_query, order_values )

            # Get the order ID of the inserted order
            order_id = cursor.lastrowid

            # Insert order items into order_items table
            order_items_query = "INSERT INTO order_items (order_id, product_id, quantity) VALUES (%s, %s, %s)"
            cursor.execute(order_items_query, (order_id, product.get_product_id(), quantity))

            # Commit the transaction
            self.connection.commit()

            # Close cursor and return True indicating successful order placement
            cursor.close()
            return True
        except Exception as err:
            print("Error while placing order:", err)
            return False

    def get_orders_by_customer(self, customer_id: int) -> List[Dict[Product, int]]:
        try:
            cursor = self.connection.cursor()
            cursor.execute("USE Ecommerce")

            # Query to fetch orders by customer ID
            query = """
                    SELECT oi.product_id, p.product_name, oi.quantity
                    FROM orders o
                    JOIN order_items oi ON o.order_id = oi.order_id
                    JOIN products p ON oi.product_id = p.product_id
                    WHERE o.customer_id = %s
                    """

            # Execute the SQL query
            cursor.execute(query, (customer_id,))

            # Fetch all rows
            rows = cursor.fetchall()

            # Initialize a list to store order details
            orders = []

            # Iterate over the rows and construct the order details
            for row in rows:
                product_id, product_name, quantity = row
                product = Product(product_id=product_id, name=product_name)
                orders.append({product: quantity})

            # Close cursor and return the list of order details
            cursor.close()
            if not orders:
                raise OrderNotFoundException(f"No orders found for customer with ID {customer_id}")
            return orders

        except Exception as err:
            print("Error while fetching orders by customer:", err)
            return []
