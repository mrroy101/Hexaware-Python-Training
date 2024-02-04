from orders import orders
from products import products

class orderDeatail(orders , products):
    def __init__(self , orderdetailID : int , orders ,  products , quantity : int):
        self.orderdetailID = orderdetailID
        self.orderID = orders
        self.productID = products
        self.product = products
        self.quantity = quantity

    def calculateSubtotal(self):
        totalAmount = self.order.totalAmount
        return totalAmount

    def getOrderDetailInfo(self):
        print(f'order deatil ID = {self.orderdetailID}')
        print(f'order id  = {self.order.orderID}')
        print(f'product id = {self.product.productID}')
        print(f'quantity = {self.quantity}')

    def UpdateQuantity(self, newQuantity):
            if newQuantity >= 0:
                self.quantity = newQuantity
            else:
                raise ValueError("Quantity cannot be negative")

    def addDiscount(self):
        pass

od1 = orderDeatail(1001 ,  1 ,101,5  )
