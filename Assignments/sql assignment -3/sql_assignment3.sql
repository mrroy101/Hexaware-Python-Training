create database HMBank;
use HMBank;

CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    DOB DATE,
    email VARCHAR(100),
    phone_number VARCHAR(15),
    address VARCHAR(255)
);

desc customers;

CREATE TABLE Accounts (
    account_id INT PRIMARY KEY,
    customer_id INT,
    account_type VARCHAR(50),
    balance DECIMAL(10, 2),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);
desc Accounts;

CREATE TABLE Transactions (
    transaction_id INT PRIMARY KEY,
    account_id INT,
    transaction_type VARCHAR(50),
    amount DECIMAL(10, 2),
    transaction_date DATE,
    FOREIGN KEY (account_id) REFERENCES Accounts(account_id)
);
desc Transactions;

INSERT INTO Customers (customer_id, first_name, last_name, DOB, email, phone_number, address)
VALUES
(1, 'Amit', 'Sharma', '1985-05-15', 'amit.sharma@example.com', '9876543210', 'New Delhi'),
(2, 'Priya', 'Patel', '1990-09-22', 'priya.patel@example.com', '8765432109', 'Mumbai'),
(3, 'Rahul', 'Mukherjee', '1988-03-10', 'rahul.m@example.com', '7654321098', 'Kolkata'),
(4, 'Neha', 'Rao', '1995-11-28', 'neha.rao@example.com', '6543210987', 'Bangalore'),
(5, 'Anjali', 'Menon', '1980-07-03', 'anjali.menon@example.com', '5432109876', 'Chennai'),
(6, 'Rajesh', 'Kumar', '1992-12-18', 'rajesh.kumar@example.com', '4321098765', 'Hyderabad'),
(7, 'Ayesha', 'Singh', '1987-06-25', 'ayesha.singh@example.com', '3210987654', 'Jaipur'),
(8, 'Vikram', 'Verma', '1993-04-07', 'vikram.verma@example.com', '2109876543', 'Pune'),
(9, 'Sunita', 'Gupta', '1984-08-14', 'sunita.gupta@example.com', '1098765432', 'Ahmedabad'),
(10, 'Arjun', 'Mehra', '1998-02-03', 'arjun.mehra@example.com', '9876543210', 'Chandigarh');

select * from customers;

INSERT INTO Accounts (account_id, customer_id, account_type, balance)
VALUES
(101, 1, 'savings', 50000.00),
(102, 2, 'current', 100000.00),
(103, 3, 'savings', 75000.00),
(104, 4, 'current', 120000.00),
(105, 5, 'zero_balance', 0.00),
(106, 6, 'savings', 30000.00),
(107, 7, 'current', 80000.00),
(108, 8, 'savings', 60000.00),
(109, 9, 'current', 90000.00),
(110, 10, 'zero_balance', 0.00);

select * from accounts;

INSERT INTO Transactions (transaction_id, account_id, transaction_type, amount, transaction_date)
VALUES
(1001, 101, 'deposit', 10000.00, '2024-01-01'),
(1002, 102, 'withdrawal', 5000.00, '2024-01-02'),
(1003, 103, 'deposit', 20000.00, '2024-01-03'),
(1004, 104, 'transfer', 15000.00, '2024-01-04'),
(1005, 105, 'deposit', 5000.00, '2024-01-05'),
(1006, 106, 'deposit', 12000.00, '2024-01-06'),
(1007, 107, 'withdrawal', 10000.00, '2024-01-07'),
(1008, 108, 'deposit', 15000.00, '2024-01-08'),
(1009, 109, 'transfer', 20000.00, '2024-01-09'),
(1010, 110, 'deposit', 8000.00, '2024-01-10');

select * from transactions;

select  accounts.customer_ID , first_name , last_name , email , account_type
from customers 
join accounts on accounts.customer_id = customers.customer_id;  

SELECT transactions.transaction_id , transactions.account_id , accounts.customer_id , first_name , last_name
FROM Transactions
JOIN Accounts ON Transactions.account_id = Accounts.account_id
JOIN Customers ON Accounts.customer_id = Customers.customer_id;


update accounts set balance = 1.1 * balance where account_type like 'savings';
select * from accounts;

SELECT CONCAT(first_name, ' ', last_name) AS full_name
FROM Customers;

DELETE FROM Accounts
WHERE balance = 0 AND account_type = 'savings';

select CONCAT(first_name ,' ' , Last_name) as fullname , address 
from customers where address like 'bangalore';

SELECT  account_id , balance
FROM Accounts
WHERE account_id = 104;

select * from accounts
where account_type like 'current'
and balance > 83124 ; -- $1000 is equal to Rs.83124

select * from transactions
having account_id = 105;

-- interest rate is 4%
SELECT account_id,balance as current_balance ,  (balance * 1.04)- balance AS accrued_interest ,
balance * 1.04 as balance_after_Interest 
FROM Accounts
WHERE account_type = 'savings';


SET @overdraft_limit = 50000.00;

SELECT *
FROM Accounts
WHERE balance < @overdraft_limit and account_type not like 'zero_balance' ;

select * from customers
where address not IN('bangalore','mumbai','pune');


select customers.customer_id , first_name , last_name , avg(balance) as avg_balance 
from accounts 
join customers where customers.customer_id = accounts.customer_id
group by customer_id;

select * from accounts 
order by balance desc
limit 10;

select transaction_id , account_id , sum(amount) as totalDeposit
from transactions 
where transaction_type like 'deposit' 
and transaction_date = '24-01-03'
group by transaction_id;

select min(dob) as oldest_customer ,
max(dob) as newest_customer
from customers;

SELECT Transactions.*, Accounts.account_type
FROM Transactions
JOIN Accounts ON Transactions.account_id = Accounts.account_id;

select customers.* , accounts.* 
from customers
join accounts on accounts.customer_ID = customers.customer_id;

SELECT Transactions.*, Customers.*
FROM Transactions
JOIN Accounts ON Transactions.account_id = Accounts.account_id
JOIN Customers ON Accounts.customer_id = Customers.customer_id
WHERE accounts.customer_id = 4;

SELECT customer_id
FROM Accounts
GROUP BY customer_id
HAVING COUNT(*) > 1;


SELECT SUM(CASE WHEN transaction_type = 'deposit' THEN amount ELSE -amount END) AS net_transaction_amount
FROM Transactions;

select transactions.account_id , avg(balance) as daily_average
from accounts
join transactions on transactions.account_id = accounts.account_id
where transaction_date between '2024-01-01' and '2024-01-05'
group by account_id;

SELECT account_type, SUM(balance) AS total_balance
FROM Accounts
GROUP BY account_type;

SELECT account_id, COUNT(transaction_id) AS transaction_count
FROM Transactions
GROUP BY account_id
ORDER BY transaction_count DESC;

SELECT Customers.customer_id, SUM(balance) AS aggregate_balance, GROUP_CONCAT(account_type) AS account_types
FROM Customers
JOIN Accounts ON Customers.customer_id = Accounts.customer_id
GROUP BY Customers.customer_id
HAVING aggregate_balance > 70000;

SELECT amount, transaction_date, account_id
FROM Transactions
WHERE (amount, transaction_date, account_id) IN (
    SELECT amount, transaction_date, account_id
    FROM Transactions
    GROUP BY amount, transaction_date, account_id
    HAVING COUNT(*) > 1
);

SELECT *
FROM Customers 
WHERE customer_id = (
    SELECT customer_id
    FROM Accounts
    ORDER BY balance DESC
    LIMIT 1
);


SELECT AVG(balance) AS avg_balance
FROM Accounts
WHERE customer_id IN (
    SELECT customer_id
    FROM Accounts
    GROUP BY customer_id
    HAVING COUNT(*) > 1
);

SELECT *
FROM Accounts
WHERE EXISTS (
    SELECT 1
    FROM Transactions
    WHERE Transactions.account_id = Accounts.account_id
    AND amount > (SELECT AVG(amount) FROM Transactions)
);


SELECT SUM(balance) AS total_balance_no_transactions
FROM Accounts
WHERE NOT EXISTS (
    SELECT 1
    FROM Transactions
    WHERE Transactions.account_id = Accounts.account_id
);

SELECT Transactions.*
FROM Transactions
JOIN Accounts ON Transactions.account_id = Accounts.account_id
WHERE Accounts.balance = (SELECT MIN(balance) FROM Accounts);

SELECT Customers.*
FROM Customers
WHERE NOT EXISTS (
    SELECT 1
    FROM Accounts
    JOIN Transactions ON Accounts.account_id = Transactions.account_id
    WHERE Accounts.customer_id = Customers.customer_id
);

SELECT Customers.*
FROM Customers
WHERE EXISTS (
    SELECT 1
    FROM Accounts
    WHERE Accounts.customer_id = Customers.customer_id
    GROUP BY account_type
    HAVING COUNT(DISTINCT account_type) > 1
);

SELECT account_type, COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Accounts) AS percentage
FROM Accounts
GROUP BY account_type;

SELECT *
FROM Transactions
join accounts on transactions.account_id = accounts.account_id
WHERE customer_id = (SELECT customer_id FROM Customers WHERE customer_id = 1);

SELECT account_type, SUM(balance) AS total_balance
FROM Accounts
GROUP BY account_type,
         (SELECT 1);