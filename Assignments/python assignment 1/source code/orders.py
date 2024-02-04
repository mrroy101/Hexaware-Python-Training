import datetime

from customers import c1
from customers import customers

class orders(customers) :
    def __init__(self , orderID : int    , customer ,  orderdate , totalAmount : float):
        self.orderID = orderID
        super().__init__(customer.customerID , customer.firstname , customer.lastname , customer.email , customer.phone , customer.address )
        #self.customer = customer
        self.orderdate = datetime.datetime.strptime(orderdate,"%Y-%m-%d").date()
        self.totalAmount = totalAmount
        self.status = 'processing'
    def calculateTotalAmount(self):
        print(f'total amount = {self.totalAmount}')
    def getOrderDetails(self):
        print(f'order id = {self.orderID}')
        print(f'customer id = {self.customerID} ')
        print(f'first name = {self.firstname} ')
        print(f'lastname = {self.lastname} ')
        print(f'order date = {self.orderdate} ')
        print(f'total amount = {self.totalAmount} ')

    def updateOrderStatus(self,status):
        self.status = status
        print(f'current status = {self.status}')

    def cancelOrder(self,orderID):
        pass



o1 = orders(1,c1,'2024-01-01',1200)
o1.getOrderDetails()
o1.updateOrderStatus('completed')
