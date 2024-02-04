class products:
    def __init__(self , productID : int ,
                 productname : str ,
                 description  : str ,
                 price : float):
        self.productID = productID
        self.productname = productname
        self.description = description
        self.price = price

    def GetProductDetail(self):
        print("product id   = " + str(self.productID))
        print("product name = " + self.productname)
        print("description  = " + self.description)
        print("price        = " + str(self.price))

    def UpdateProductInfo(self , newprice , newdesc):
        self.price = newprice
        self.description = newdesc

    def IsProductInStock(self):
        pass


p1 = products(
    12 , 'telivision' ,
    'electronic gadget' ,
    1299.00
)

#p1.GetProductDetail()




