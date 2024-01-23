create database CarRental;
use CarRental;

create table vehicle(vehicleID int primary key,
make varchar(100),
model varchar(100),
year year,
dailyRate float(5,2),
status varchar(100) check(status in ('available' , 'not available')),
passengerCapacity int,
engineCapacity int);

desc vehicle;

create table customer(customerID int primary key ,
firstname varchar(100),
lastname varchar(100),
email varchar(100),
phoneNumber varchar(20));
desc customer;

create table lease(leaseID int primary key,
vehicleID int ,
customerID int ,
startDate date ,
endDate date ,
type varchar(15) check(type in ('daily', 'monthly')),
foreign key (vehicleID) references vehicle(vehicleID),
foreign key (customerID) references customer(customerID));

desc lease;

create table payment(paymentID int primary key,
leaseID int,
paymentDate date ,
amount float(10,2),
foreign key (leaseID) references lease(leaseID));

desc payment;

insert into vehicle values
(1 , 'toyota', 'camry' , 2022 , 50.00 , 'available' , 4 , 1450) ,
(2 , 'honda', 'civic' , 2023 , 45.00 , 'available' ,7 , 1500) ,
(3,'ford', 'focus' ,  2022 , 48.00 , 'not available' ,4 , 1400) ,
(4 , 'nissan', 'altima' , 2023 , 52.00 , 'available' , 7 , 1200) ,
(5 , 'chevrolet' , 'malibu' , 2022 , 47.00 , 'available' , 4 , 1800) ,
(6 ,'hyundai', 'sonata' ,2023 , 49.00 , 'not available' , 7 , 1400) ,
(7 , 'BMW' , '3 series' ,2023 , 60.00 , 'available' , 7 , 2499),
(8 ,'mercedes', 'c-class' ,2022 , 58.00 , 'available' , 8 , 2599),
(9 ,'Audi' , 'A4' ,2022 , 55.00 , 'not available' , 4 , 2500),
(10 , 'lexus' , 'ES' ,2023 , 54.00 , 'available' , 4 , 2500);

select * from vehicle ;

insert into customer values 
(1,'john','doe','johndoe@example.com', '555-555-5555-'),
(2,'jane','smith','janesmith@example.com','555-123-4567'),
(3,'robert','johnson','robert@example.com','555-789-1234'),
(4,'sarah','brown','sarah@example.com','555-456-7890'),
(5,'david','lee','david@example.com','555-987-6543'),
(6,'laura','hall','laura@example.com','555-234-5678'),
(7,'michael','davis','michael@example.com','555-876-5432'),
(8,'emma','wilson','emma@example.com','555-432-1098'),
(9,'william','taylor','william@example.com','555-321-6547'),
(10,'olivia','adams','olivia@example.com','555-765-4321');

select * from customer;

insert into lease values
(1,1,1,'2023-01-01','2023-01-05','daily'),
(2,2,2,'2023-02-15','2023-02-28','monthly'),
(3,3,3,'2023-03-10','2023-03-15','daily'),
(4,4,4,'2023-04-20','2023-04-30','monthly'),
(5,5,5,'2023-05-05','2023-05-10','daily'),
(6,4,3,'2023-06-15','2023-06-30','monthly'),
(7,7,7,'2023-07-01','2023-07-10','daily'),
(8,8,8,'2023-08-12','2023-08-15','monthly'),
(9,3,3,'2023-09-07','2023-09-10','daily'),
(10,10,10,'2023-10-10','2023-10-31','monthly');
 select * from lease;
 
 insert into payment values
 (1,1,'2023-01-03',200.00),
 (2,2,'2023-02-20',1000.00),
 (3,3,'2023-03-12',75.00),
 (4,4,'2023-04-25',900.00),
 (5,5,'2023-05-07',60.00),
 (6,6,'2023-06-18',1200.00),
 (7,7,'2023-07-03',40.00),
 (8,8,'2023-08-14',1100.00),
 (9,9,'2023-09-09',80.00),
 (10,10,'2023-10-25',1500.00);
 
 select * from payment;

update vehicle set dailyrate = 68.00 where make = 'mercedes';
select * from vehicle where make = 'mercedes';

delete from customer
where customerID =9;

alter table payment
rename column paymentdate to transactionDate ;
desc payment;

select * from customer where email like 'michael@example.com' ;


set @date1 = '2023-04-25'; -- current date is of 2024 so made a variable for current date and added date to show a set
select * from lease 
join customer on customer.customerID = lease.customerID
where customer.firstname = 'sarah' and enddate >= @date1; 

select payment.* 
from payment
join lease on payment.leaseid = lease.leaseid
join customer on customer.customerid = lease.customerid
where customer.phonenumber = '555-987-6543';

delete from payment 
where leaseID in(select leaseID from lease where customerID = 7);
select * from payment;

delete from lease 
where customerID = 7;
select * from lease;

delete from customer
where customerID = 7;
select * from customer;


select make , model , avg(dailyrate) as avgDailyRates
from vehicle 
where status = 'available'
group by vehicleID;

select make , model , dailyrate as highest_daily_rate
from vehicle
group by vehicleID
order by dailyrate desc
limit 1;


select * 
from vehicle 
where vehicleID in(
select lease.vehicleID
from lease
where lease.customerID = 3
);

select * 
from lease 
order by startdate desc 
limit 1;

select *
from payment
where year(transactiondate) = 2023;

select * from customer
where customerid not in(select customer.customerID from customer
join lease on lease.customerid = customer.customerid
where lease.leaseID  in(select leaseID from payment
where leaseID = payment.leaseID)) ;


select vehicle.* , sum(payment.amount) as totalAmount
from vehicle 
join lease on vehicle.vehicleID = lease.vehicleID
join payment on payment.leaseid = lease.leaseID
group by vehicleID;


select customer.* , sum(payment.amount) as totalAmount
from customer
join lease on customer.customerID = lease.customerID
join payment on payment.leaseid = lease.leaseID
group by customerID;

select vehicle.* , lease.*
from vehicle 
join lease on  lease.vehicleID = vehicle.vehicleID;

select lease.*, customer.*, vehicle.*
from lease
join customer on lease.customerid = customer.customerid
join vehicle on lease.vehicleid = vehicle.vehicleid
where '2023-06-20' between startdate and enddate; 


select customer.* , sum(payment.amount) as totalAmount
from customer
join lease on customer.customerID = lease.customerID
join payment on payment.leaseid = lease.leaseID
group by customerID
order by totalamount desc
limit 1 ;


set @curdate1 = '2023-05-15';  -- as current date has no active rent so i am using current date as 2023-05-15
select vehicle.* , lease.* 
from vehicle 
join lease on vehicle.vehicleID = lease.vehicleID
where enddate > @curdate1;