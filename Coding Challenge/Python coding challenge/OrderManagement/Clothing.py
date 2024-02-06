from OrderManagement.Product import Product

class Clothing(Product):
    def __init__(self, productId, productName, description, price, quantityInStock, type, size, color):
        super().__init__(productId, productName, description, price, quantityInStock, type)
        self.size = size
        self.color = color

    @property
    def getSize(self):
        return self.size

    @getSize.setter
    def setSize(self, size):
        self.size = size

    @property
    def getColor(self):
        return self.color

    @getColor.setter
    def setColor(self, color):
        self.color = color


c1 = Clothing(1, "T-shirt", "Casual wear", 20.0, 100, "Clothing", "M", "Blue")
print(c1.getColor)