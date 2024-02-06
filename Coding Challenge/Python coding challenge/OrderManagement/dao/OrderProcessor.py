from OrderManagement.dao import IOrderManagementRepository
from OrderManagement.Exception.custome_exception import OrderNotFound, UserNotFound


class OrderProcessor(IOrderManagementRepository):
    def __init__(self, DBUtil):
        self.dbutil = DBUtil

    def createUser(self, user):
        try:
            conn = self.dbutil.getDBConnection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (userId, username, password, role) VALUES (%s, %s, %s, %s)",
                           (user.userId, user.username, user.password, user.role))
            conn.commit()

            cursor.close()
            conn.close()

            print("User created successfully.")
        except Exception as e:
            print("Error creating user:", e)
            conn.rollback()


    def createOrder(self):
        global conn
        try:
            conn = self.dbutil.getDBConnection()
            cursor = conn.cursor()

            orderId = int(input("Enter the order ID: "))
            productId = int(input("Enter the product ID: "))
            userId = int(input("Enter the user ID: "))

            cursor.execute("INSERT INTO orders (orderId, productId, userId) VALUES (%s, %s, %s) "
                           "RETURNING orderId", (orderId, productId, userId))
            order_id = cursor.fetchone()[0]
            conn.commit()

            cursor.close()
            conn.close()

            return order_id
        except Exception as e:
            print("Error creating order:", e)
            conn.rollback()
            return None


    def cancelOrder(self, orderId, userId):
        try:
            conn = self.dbutil.getDBConnection()
            cursor = conn.cursor()

            cursor.execute("SELECT orderId FROM orders WHERE orderId = %s AND userId = %s", (orderId, userId))
            if not cursor.fetchone():
                raise OrderNotFound(f"Order with ID {orderId} not found for user with ID {userId}")

            cursor.execute("DELETE FROM orders WHERE orderId = %s AND userId = %s", (orderId, userId))
            conn.commit()

            cursor.close()
            conn.close()

            print("Order successfully cancelled.")
        except OrderNotFound as e:
            print(e)
        except Exception as e:
            print("Error cancelling order:", e)
            conn.rollback()

    def createProduct(self, user, product):
        global conn
        try:
            conn = self.dbutil.getDBConnection()
            cursor = conn.cursor()


            cursor.execute("SELECT role FROM users WHERE userId = %s", (user.userId,))
            user_role = cursor.fetchone()
            if not user_role or user_role[0] != "Admin":
                raise UserNotFound("User is not an admin.")

            cursor.execute(
                "INSERT INTO products (productId, productName, description,"
                " price, quantityInStock, type) VALUES (%s, %s, %s, %s, %s, %s)",
                (product.productId, product.productName, product.description, product.price, product.quantityInStock,
                 product.type))
            conn.commit()

            cursor.close()
            conn.close()

            print("Product created successfully.")
        except UserNotFound as e:
            print(e)
        except Exception as e:
            print("Error creating product:", e)
            conn.rollback()

    def getAllProducts(self):
        try:
            conn = self.dbutil.getDBConnection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM products")
            products = cursor.fetchall()

            cursor.close()
            conn.close()

            print("All products retrieved successfully.")
            return products
        except Exception as e:
            print("Error retrieving products:", e)
            return None

    def getOrderByUser(self, user):
        try:
            conn = self.dbutil.getDBConnection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM orders WHERE userId = %s", (user.userId,))
            orders = cursor.fetchall()

            cursor.close()
            conn.close()

            print(f"All orders for user {user.username} retrieved successfully.")
            return orders
        except Exception as e:
            print("Error retrieving orders:", e)
            return None