class Product:

    def __init__(self, productId, productName, description, price, quantityInStock, type):
        self.productId = productId
        self.productName = productName
        self.description = description
        self.price = price
        self.quantityInStock = quantityInStock
        self.setType(type)

    @property
    def getProductId(self):
        return self.productId

    @property
    def getProductName(self):
        return self.productName

    @property
    def getDescription(self):
        return self.description

    @property
    def getPrice(self):
        return self.price

    @property
    def getQuantityInStock(self):
        return self.quantityInStock

    @property
    def getType(self):
        return self.type

    def setProductId(self, productId):
        self.productId = productId

    def setProductName(self, productName):
        self.productName = productName

    def setDescription(self, description):
        self.description = description

    def setPrice(self, price):
        self.price = price

    def setQuantityInStock(self, quantityInStock):
        self.quantityInStock = quantityInStock

    def setType(self, type):
        if type not in ['Electronics', 'Clothing']:
            raise Exception("You have entered wrong type: please choose between Electronics and Clothing")
        self.type = type


p1 = Product(1, 'smart watch', 'wearable', 1299, 50, 'Clothing')
#print(p1.getProductName)
#p1.setType('Electronics')
#print(p1.getType)