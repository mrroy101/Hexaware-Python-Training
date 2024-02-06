from OrderManagement.Product import Product

class Electronics(Product):
    def __init__(self, productId, productName, description, price, quantityInStock, type, brand, warrantyPeriod):
        super().__init__(productId, productName, description, price, quantityInStock, type)
        self.brand = brand
        self.warrantyPeriod = warrantyPeriod

    @property
    def getBrand(self):
        return self.brand

    def setBrand(self, brand):
        self.brand = brand

    @property
    def getWarrantyPeriod(self):
        return self.warrantyPeriod

    def setWarrantyPeriod(self, warrantyPeriod):
        self.warrantyPeriod = warrantyPeriod

e1 = Electronics(12, 'smartphone', 'cell phone', 29999, 70, 'Electronics', 'oneplus', 2)
print(e1.getWarrantyPeriod)  # Note: Accessing property like a method
