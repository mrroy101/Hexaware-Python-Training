CREATE DATABASE TechShop;
USE TechShop;

-- Customers Table
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    Phone VARCHAR(20),
    Address VARCHAR(255)
);

-- Products Table
CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    Description TEXT,
    Price DECIMAL(10, 2)
);

-- Orders Table
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    TotalAmount DECIMAL(10, 2),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- OrderDetails Table
CREATE TABLE OrderDetails (
    OrderDetailID INT PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    Quantity INT,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Inventory Table
CREATE TABLE Inventory (
    InventoryID INT PRIMARY KEY,
    ProductID INT,
    QuantityInStock INT,
    LastStockUpdate TIMESTAMP,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);


-- Inserting more sample data into Customers table
INSERT INTO Customers VALUES
(1, 'John', 'Doe', 'john.doe@email.com', '1234567890', '123 Main St'),
(2, 'Jane', 'Smith', 'jane.smith@email.com', '9876543210', '456 Oak St'),
(3, 'Alice', 'Johnson', 'alice.j@email.com', '5551112233', '789 Pine St'),
(4, 'Bob', 'Williams', 'bob.w@email.com', '3339998877', '654 Elm St'),
(5, 'Eva', 'Miller', 'eva.m@email.com', '7774445566', '987 Cedar St'),
(6, 'Chris', 'Brown', 'chris.b@email.com', '2228886655', '321 Birch St'),
(7, 'Olivia', 'Davis', 'olivia.d@email.com', '1114447777', '456 Maple St'),
(8, 'Daniel', 'Clark', 'daniel.c@email.com', '8887771111', '789 Oak St'),
(9, 'Sophia', 'Wilson', 'sophia.w@email.com', '9996663333', '234 Pine St'),
(10, 'Michael', 'Moore', 'michael.m@email.com', '6662228888', '567 Cedar St');

-- Inserting more sample data into Products table
INSERT INTO Products VALUES
(1, 'Laptop', 'High-performance laptop', 999.99),
(2, 'Smartphone', 'Latest smartphone model', 499.99),
(3, 'Tablet', 'High-end tablet with stylus', 699.99),
(4, 'Smartwatch', 'Fitness and health tracking', 199.99),
(5, 'Desktop PC', 'Powerful desktop computer', 1299.99),
(6, 'Headphones', 'Noise-canceling wireless headphones', 149.99),
(7, 'Printer', 'Color laser printer', 299.99),
(8, 'Camera', 'Mirrorless digital camera', 899.99),
(9, 'External Hard Drive', '2TB USB 3.0 hard drive', 79.99),
(10, 'Gaming Console', 'Latest gaming console', 499.99);


INSERT INTO Orders VALUES
(1, 1, '2024-01-12', 1500.50),
(2, 2, '2024-01-13', 800.75),
(3, 3, '2024-01-14', 300.25),
(4, 4, '2024-01-15', 500.50),
(5, 5, '2024-01-16', 120.90),
(6, 6, '2024-01-17', 800.25),
(7, 7, '2024-01-18', 250.60),
(8, 8, '2024-01-19', 400.75),
(9, 9, '2024-01-20', 600.30),
(10, 10, '2024-01-21', 900.45);


INSERT INTO OrderDetails VALUES
(1, 1, 1, 2),
(2, 1, 2, 1),
(3, 3, 3, 1),
(4, 4, 4, 2),
(5, 5, 5, 3),
(6, 6, 6, 1),
(7, 7, 7, 2),
(8, 8, 8, 1),
(9, 9, 9, 2),
(10, 10, 10, 3);


INSERT INTO Inventory VALUES
(1, 1, 10, '2024-01-12 10:00:00'),
(2, 2, 20, '2024-01-13 11:30:00'),
(3, 3, 5, '2024-01-14 09:30:00'),
(4, 4, 8, '2024-01-15 12:45:00'),
(5, 5, 15, '2024-01-16 10:15:00'),
(6, 6, 3, '2024-01-17 14:20:00'),
(7, 7, 10, '2024-01-18 11:00:00'),
(8, 8, 7, '2024-01-19 13:30:00'),
(9, 9, 12, '2024-01-20 15:45:00'),
(10, 10, 6, '2024-01-21 08:00:00');


show tables;
Select * from Customers;
Select * from Products;
Select * from orders;
Select * from orderdetails;
Select * from inventory;

select firstname , lastname , email from customers;

SELECT  Orders.OrderDate, Customers.FirstName, Customers.LastName
FROM Orders
JOIN Customers ON Orders.CustomerID = Customers.CustomerID;


insert into customers values( 11 , "Carl" , "Johnson", "carl.j@email.com" , 8877665544 , "987 perk st");
select * from customers where customerId = 11;


UPDATE Products
SET Price = Price * 1.1;

show tables;

delimiter @@
CREATE PROCEDURE DeleteCustomerOrders(IN CustomerIDParam INT)
BEGIN
    -- Delete from OrderDetails
    DELETE FROM OrderDetails
    WHERE OrderID IN (SELECT OrderID FROM Orders WHERE CustomerID = CustomerIDParam);

    -- Delete from Orders
    DELETE FROM Orders WHERE CustomerID = CustomerIDParam;
end @@

delimiter ;
set @m = '3';
call DeleteCustomerOrders(@m);

select * from customers;









delimiter @@
create procedure UpdateEmail1(INout NewEmail text ,INOUT UpdateCust_ID int)
begin
	update customers set email = NewEmail where CustomerID = UpdateCust_ID;
    
end @@

delimiter ;
set @E = 'new.email@email.com' ;
set @id = '1';
call UpdateEmail1(@E , @id);

select * from customers where customerID = 1;


desc orders;

SELECT orders.CustomerID, FirstName, LastName, COUNT(OrderID) AS OrderCount
FROM Orders
JOIN Customers ON Orders.CustomerID = Customers.CustomerID
GROUP BY CustomerID, FirstName, LastName;



SELECT OrderDetails.productID , ProductName, SUM(Quantity) AS TotalQuantityOrdered
FROM OrderDetails
JOIN Products ON OrderDetails.ProductID = Products.ProductID
GROUP BY ProductID, ProductName
ORDER BY TotalQuantityOrdered DESC
LIMIT 1;


SELECT ProductName, description
FROM Products;

SELECT Customers.CustomerID, FirstName, LastName, AVG(TotalAmount) AS AverageOrderValue
FROM Orders
JOIN Customers ON Orders.CustomerID = Customers.CustomerID
GROUP BY Customers.CustomerID, FirstName, LastName;


SELECT OrderID, OrderDate, FirstName, LastName, MAX(TotalAmount) AS MaxTotalRevenue
FROM Orders
JOIN Customers ON Orders.CustomerID = Customers.CustomerID
group by orderID
order by MAxTotalRevenue desc 
limit 1;



SELECT products.ProductID, ProductName, COUNT(OrderDetails.OrderID) AS OrderCount
FROM Products
LEFT JOIN OrderDetails ON Products.ProductID = OrderDetails.ProductID
GROUP BY ProductID, ProductName;

delimiter @@
create procedure CheckOrderPerson3(INOUT ProdName varchar(50))
begin 
	SELECT FirstName, LastName, Email
	FROM Customers
	WHERE CustomerID IN (
    SELECT DISTINCT Orders.CustomerID
    FROM Orders
    JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
    WHERE OrderDetails.ProductID = (SELECT ProductID FROM Products WHERE ProductName like ProdName)
);
end @@

delimiter ;
set @pname = 'laptop' ;
call CheckOrderPerson1(@pname);



	SELECT FirstName, LastName, Email
	FROM Customers
	WHERE CustomerID IN (
    SELECT DISTINCT Orders.CustomerID
    FROM Orders
    JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
    WHERE OrderDetails.ProductID = (SELECT ProductID FROM Products WHERE ProductName = 'laptop' ));
    
    
    
delimiter @@
create procedure TotalRevenueForTimePeriod3(IN date1 date , IN date2 date)
begin
    SELECT SUM(TotalAmount) AS TotalRevenue
	FROM Orders
	WHERE OrderDate BETWEEN date1 AND date2;
end @@

delimiter ;
call TotalRevenueForTimePeriod3('2024-01-15' , '2024-01-20'); 


INSERT INTO Customers VALUES
(12, 'Tommy', 'Versatty', 'tommy.v@email.com', '2222222222', '222 sun St');


SELECT CustomerID, FirstName, LastName
FROM Customers
WHERE CustomerID NOT IN (SELECT DISTINCT CustomerID FROM Orders);


select count(productname) as totalProduct from products;

select sum(totalAmount) as TotalRevenue from orders;



delimiter @@
create procedure ShowAverageQuantity(IN category varchar(50))
begin

	SELECT AVG(Quantity) AS AverageQuantityOrdered
	FROM OrderDetails
	JOIN Products ON OrderDetails.ProductID = Products.ProductID
	WHERE productname = category;
    
end @@

delimiter ;
call ShowAverageQuantity('Laptop');


delimiter @@
create procedure RevenuePerCustomer1(in id int)
begin

	SELECT customers.CustomerID, FirstName, LastName, SUM(TotalAmount) AS TotalRevenue
	FROM Orders 
	join customers on orders.customerID = customers.customerID 
	WHERE orders.CustomerID = id
    group by orders.customerID;
end @@

delimiter ;
call RevenuePerCustomer1(2);



select customers.customerid , firstname , lastname ,  count(orderID) as orderCount 
from orders
join customers on orders.customerID = customers.customerID
group by orderid
order by orderCount desc 
limit 1;


/* 7.	Write an SQL query to find the most popular product category, 
which is the one with the highest total quantity ordered across all orders.
*/

SELECT orderdetails.productID, SUM(Quantity) AS TotalQuantityOrdered
FROM OrderDetails
JOIN Products ON OrderDetails.ProductID = Products.ProductID
GROUP BY productID
ORDER BY TotalQuantityOrdered DESC
LIMIT 1;


select customers.customerID , firstname , lastname , sum(totalAmount) as totalSpent
from customers 
join orders on orders.customerID = customers.customerID
group by customerID
order by totalspent desc
limit 1;

SELECT customers.CustomerID, FirstName, LastName, AVG(TotalAmount) AS AverageOrderValue
FROM Orders
JOIN Customers ON Orders.CustomerID = Customers.CustomerID
GROUP BY CustomerID, FirstName, LastName;


select customers.customerID , firstname , lastname , count(orderID) as totalOrders
from customers 
join orders on customers.customerID = orders.customerID
group by customerID;