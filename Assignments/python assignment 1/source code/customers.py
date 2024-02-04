import re
class customers:
    def __init__(self , customerID : int ,
                 firstname : str ,
                 lastname : str ,
                 email : str,
                 phone : str,
                 address : str):
        self.customerID = customerID
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phone = phone
        self.address = address
        self.totalorders = 0

    def CalculateTotalOrders(self):
        return self.totalorders
    def GetCustomerDetails(self):
        print("customerID  : " + str(self.customerID))
        print("firstname   : " + self.firstname)
        print("lastname    : " + self.lastname)
        print("email       : " + self.email)
        print("phone       : " + self.phone)
        print("address     : " + self.address)
    def UpdateCustomerInfo(self , new_email , new_phone , new_add ):
        self.email = new_email
        self.phone = new_phone
        self.address = new_add


    def checkEmail(self , email):
        pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if re.match(pat, email):
            print("Valid Email")
        else:
            raise Exception("Invalid Email")



c1 = customers(101,'sankar' , 'roy' ,
               'sankarray101@gmail.com' , '7008673976' ,
               'sunabeda , koraput')
#c1.GetCustomerDetails()
#print(c1.CalculateTotalOrders())
#c1.UpdateCustomerInfo('sankarroy.ele.2019@gmail.com' ,
  ##                    'sunabeda')
#c1.GetCustomerDetails()
