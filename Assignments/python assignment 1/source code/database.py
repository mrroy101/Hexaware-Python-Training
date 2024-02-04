import mysql.connector

con = mysql.connector.connect(
        host= "localhost" ,
        user = "root" ,
        password  = "root",
        port = "3306",
        database = "TechShopDB"
        )


cur = con.cursor()
cur.execute("show tables")
id = int(11)
firstname = 'sankar'
lastname = 'roy'
email='sankarray101@gmail.com'
phone = '7008673976'
address = 'sunabeda , koraput'

data1=(id,firstname,lastname,email,phone,address)
print(data1)
str1 = "insert into Customers values(%s,%s,%s,%s,%s,%s)"
cur.execute(str1,data1)