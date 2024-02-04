import datetime

from products import products
from products import p1


class inventory(products):
    def __init__(self, inventoryID: int, product, quantityInStock: int, lastStockUpdate: int):
        self.inventoryID = inventoryID
        super().__init__(product.productID , product.productname ,product.description,product.price)
        self.quantityInStock = quantityInStock
        self.lastStockUpdate = lastStockUpdate

    def getProduct(self):
        print(f"Inventory Id = {self.inventoryID}")
        print(f"Product Id = {self.productID}")
        print(f"Product Name = {self.productname}")
        print(f"Product Description = {self.description}")
        print(f"Product Price = {self.price}")

    def getQuantityInStock(self):
        return self.quantityInStock

    def addToInventory(self, quantity):
        self.quantityInStock += quantity

    def removeFromInventory(self, quantity):
            if quantity <= self.quantityInStock:
                self.quantityInStock -= quantity
                self.lastStockUpdate = self.quantityInStock
            else:
                raise ValueError("cannot remove this quantity")


    def updateStockQuantity(self, newquantity):
            if newquantity >= 0:
                self.quantityInStock += newquantity
                self.lastStockUpdate = self.quantityInStock
            else:
                raise ValueError("Quanitity cannot be negative.")


    def isProductAvailable(self, quantity):
        if quantity >= self.quantityInStock:
            print("yes the product is available")
        else:
            print("the product is not available")

    def getInventoryValue(self):
        return self.quantityInStock * self.price

    def listLowStockProducts(self, minStock):
        if self.quantityInStock < minStock:
            print(f" {self.productName} is low in quantity")
        else:
            print("stock available")

    def listOutOfStockProducts(self):
        pass

    def listAllProducts(self):
        pass

i1 = inventory(501 , p1 , 67 , 52)
i1.getProduct()
print(i1.getInventoryValue())