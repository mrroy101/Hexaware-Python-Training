CREATE DATABASE TicketBookingSystem;
USE TicketBookingSystem;


CREATE TABLE Venue (
    venue_id INT PRIMARY KEY,
    venue_name VARCHAR(255),
    address VARCHAR(255)
);

desc Venue;


CREATE TABLE Event (
    event_id INT PRIMARY KEY,
    event_name VARCHAR(255),
    event_date DATE,
    event_time TIME,
    venue_id INT,
    total_seats INT,
    available_seats INT,
    ticket_price DECIMAL,
    event_type  varchar(100) check(event_type in ('movie','sports','concert')),
    booking_id INT
    -- FOREIGN KEY (venue_id) REFERENCES Venue(venue_id),
    -- FOREIGN KEY (booking_id) REFERENCES Booking(booking_id)
);

desc Event;

CREATE TABLE Customer (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(255),
    email VARCHAR(255),
    phone_number VARCHAR(15),
    booking_id INT
    -- FOREIGN KEY (booking_id) REFERENCES Booking(booking_id)
);

desc Customer;

CREATE TABLE Booking (
    booking_id INT PRIMARY KEY,
    customer_id INT,
    event_id INT,
    num_tickets INT,
    total_cost DECIMAL,
    booking_date DATE
    -- FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
   -- FOREIGN KEY (event_id) REFERENCES Event(event_id)
);

desc booking;

alter table Event add constraint foreign key (venue_id) REFERENCES Venue(venue_id);
alter table Event add constraint foreign key (booking_id) REFERENCES Booking(booking_id);
alter table Customer add constraint foreign key (booking_id) REFERENCES Booking(booking_id);
alter table booking add constraint foreign key (customer_id) REFERENCES Customer(customer_id);
alter table booking add constraint foreign key (event_id) REFERENCES Event(event_id);

INSERT INTO Venue (venue_id, venue_name, address) VALUES
(1, 'Mumbai Exhibition Center', '123 Exhibition Road, Mumbai'),
(2, 'Delhi Sports Complex', '456 Sports Avenue, Delhi'),
(3, 'Chennai Concert Hall', '789 Music Street, Chennai'),
(4, 'Bangalore Movie Theater', '101 Film Lane, Bangalore'),
(5, 'Kolkata Convention Center', '202 Convention Road, Kolkata'),
(6, 'Hyderabad Stadium', '303 Sports Street, Hyderabad'),
(7, 'Jaipur Entertainment Plaza', '404 Entertainment Road, Jaipur'),
(8, 'Ahmedabad Arena', '505 Arena Lane, Ahmedabad'),
(9, 'Pune Cultural Center', '606 Cultural Street, Pune'),
(10, 'Lucknow Pavilion', '707 Pavilion Road, Lucknow');

select * from venue;

INSERT INTO Event (event_id, event_name, event_date, event_time, total_seats, available_seats, ticket_price, event_type) VALUES
(1, 'Cricket Match', '2024-02-15', '18:00:00', 25000, 15000, 500, 'Sports'),
(2, 'Bollywood Night', '2024-03-10', '20:00:00',  5000, 3000, 1000, 'Concert'),
(3, 'Movie Premiere', '2024-04-05', '19:30:00',  1000, 800, 150, 'Movie'),
(4, 'Tech Expo', '2024-05-20', '10:00:00',  1500, 1200, 200, 'movie'),
(5, 'Kabaddi Championship', '2024-06-15', '17:30:00',  12000, 8000, 300, 'Sports'),
(6, 'Classical Music Concert', '2024-07-08', '19:00:00',  2000, 1500, 500, 'Concert'),
(7, 'Comedy Show', '2024-08-25', '21:00:00',  3000, 2500, 150, 'movie'),
(8, 'Drama Play', '2024-09-18', '18:30:00',  800, 600, 100, 'movie'),
(9, 'Football Match', '2024-10-12', '11:30:00',  5000, 4000, 50, 'sports'),
(10, 'Rock Band Concert', '2024-11-30', '22:00:00',  7000, 5000, 200, 'Concert');

select * from Event;

INSERT INTO Customer (customer_id, customer_name, email, phone_number) VALUES
(1, 'Rajesh Kumar', 'rajesh@example.com', '9876543210'),
(2, 'Priya Singh', 'priya@example.com', '8765432109'),
(3, 'Amit Sharma', 'amit@example.com', '7654321098'),
(4, 'Sneha Verma', 'sneha@example.com', '6543210987'),
(5, 'Vikram Singh', 'vikram@example.com', '5432109876'),
(6, 'Pooja Gupta', 'pooja@example.com', '4321098765'),
(7, 'Rahul Kapoor', 'rahul@example.com', '3210987654'),
(8, 'Neha Singh', 'neha@example.com', '2109876543'),
(9, 'Sanjay Patel', 'sanjay@example.com', '1098765432'),
(10, 'Kavita Joshi', 'kavita@example.com', '9876543210');



INSERT INTO Booking (booking_id, customer_id, event_id, num_tickets, total_cost, booking_date) VALUES
(1, 1, 1, 5, 2500, '2024-02-10'),
(2, 2, 2, 3, 3000, '2024-03-05'),
(3, 3, 3, 2, 300, '2024-04-01'),
(4, 4, 5, 6, 1800, '2024-06-01'),
(5, 5, 6, 4, 2000, '2024-07-05'),
(6, 6, 7, 2, 300, '2024-08-20'),
(7, 7, 8, 1, 100, '2024-09-15'),
(8, 8, 10, 3, 600, '2024-11-25'),
(9, 9, 4, 10, 2000, '2024-05-15'),
(10, 10, 9, 5, 250, '2024-10-01');

update event set booking_id = 1 where event_id = 1;
update event set booking_id = 2 where event_id = 2;
update event set booking_id = 3 where event_id = 3;
update event set booking_id = 4 where event_id = 4;
update event set booking_id = 5 where event_id = 5;
update event set booking_id = 6 where event_id = 6;
update event set booking_id = 7 where event_id = 7;
update event set booking_id = 8 where event_id = 8;
update event set booking_id = 9 where event_id = 9;
update event set booking_id = 10 where event_id = 10;

update event set venue_id = 2 where event_id = 1;
update event set venue_id = 3 where event_id = 2;
update event set venue_id = 4 where event_id = 3;
update event set venue_id = 1 where event_id = 4;
update event set venue_id = 6 where event_id = 5;
update event set venue_id = 5 where event_id = 6;
update event set venue_id = 7 where event_id = 7;
update event set venue_id = 9 where event_id = 8;
update event set venue_id = 8 where event_id = 9;
update event set venue_id = 10 where event_id = 10;

select * from customer;

update customer set booking_id = 1 where customer_id = 1;
update customer set booking_id = 2 where customer_id = 2;
update customer set booking_id = 3 where customer_id = 3;
update customer set booking_id = 4 where customer_id = 4;
update customer set booking_id = 5 where customer_id = 5;
update customer set booking_id = 6 where customer_id = 6;
update customer set booking_id = 7 where customer_id = 7;
update customer set booking_id = 8 where customer_id = 8;
update customer set booking_id = 9 where customer_id = 9;
update customer set booking_id = 10 where customer_id = 10;

select distinct * from  event;

SELECT * FROM Event WHERE available_seats > 0;

select event_name from event where event_name like '%cup%';

select * from event where ticket_price between 1000 and 2500;

select * from event where event_date between '2024-05-20' and '2024-08-25';

SELECT * FROM Event WHERE available_seats > 0 AND event_name like '%Concert';

SELECT * FROM Customer LIMIT 5 OFFSET 5;

select * from booking where num_tickets >4;

select * from customer where phone_number = "%000";

select * from event having total_seats > 15000
order by total_seats;

SELECT * FROM Event WHERE event_name NOT LIKE 'x%' or event_name NOT LIKE 'y%' or event_name NOT LIKE 'z%';


SELECT event_name, AVG(ticket_price) AS average_ticket_price
FROM Event
GROUP BY event_name;

SELECT event_name, SUM(total_cost) AS total_revenue
FROM Booking
JOIN Event ON Booking.event_id = Event.event_id
GROUP BY event_name;


select event.event_name , sum(num_tickets) as ticketSold 
from booking
join event on booking.event_id = event.event_id
group by event_name
order by ticketSold desc
limit 1;

select event.event_name , sum(num_tickets) as ticketSold 
from booking
join event on booking.event_id = event.event_id
group by event_name
order by ticketSold;

select event.event_name 
from booking
join event on event.event_id = booking.event_id 
where num_tickets is null
group by event_name;

select * from booking;


select customer.customer_name , sum(num_tickets) as TicketBooked 
from booking 
join customer on customer.customer_id = booking.customer_id
group by customer_name
order by TicketBooked desc
limit 1;

SELECT event.event_name , DATE_FORMAT(booking.booking_date, '%Y-%m') AS month, count(booking.booking_id) AS total_tickets_sold
FROM Booking
join event on event.event_id = booking.event_id
GROUP BY booking.booking_id;


select event.event_name , avg(ticket_price) as avgPrice 
from venue 
join event on venue.venue_id = event.venue_id
group by event_name;


SELECT event_type, SUM(num_tickets) AS total_tickets_sold
FROM Booking
JOIN Event ON Booking.event_id = Event.event_id
GROUP BY event_type;


SELECT YEAR(booking_date) AS year, SUM(total_cost) AS total_revenue
FROM Booking
GROUP BY year;


SELECT customer_name, COUNT(DISTINCT Booking.event_id) AS events_booked
FROM Customer
JOIN Booking ON Customer.customer_id = Booking.customer_id
GROUP BY customer_name
HAVING events_booked > 1;

SELECT customer_name, SUM(total_cost) AS total_revenue
FROM Customer
JOIN Booking ON Customer.customer_id = Booking.customer_id
GROUP BY customer_name;

SELECT venue_id, event_type, AVG(ticket_price) AS average_ticket_price
FROM Event
GROUP BY venue_id, event_type;


SELECT customer_name, SUM(num_tickets) AS total_tickets_purchased
FROM Customer
JOIN Booking ON Customer.customer_id = Booking.customer_id
WHERE booking_date >= CURDATE() - INTERVAL 30 DAY
GROUP BY customer_name;


SELECT venue_id, AVG(ticket_price) AS average_ticket_price
FROM Event
WHERE venue_id IN (SELECT DISTINCT venue_id FROM Event)
GROUP BY venue_id;


SELECT event_name
FROM Event
WHERE event_id IN (
    SELECT event_id
    FROM Booking
    GROUP BY event_id
    HAVING SUM(num_tickets) > 0.5 * total_seats
);

SELECT event_name,
    (SELECT SUM(num_tickets) FROM Booking WHERE Event.event_id = Booking.event_id) AS total_tickets_sold
FROM Event;


SELECT customer_name
FROM Customer
WHERE NOT EXISTS (SELECT 1 FROM Booking WHERE Customer.customer_id = Booking.customer_id);

SELECT event_name
FROM Event
WHERE event_id NOT IN (SELECT DISTINCT event_id FROM Booking);



SELECT event_type, SUM(total_tickets_sold) AS total_tickets_sold
FROM (
    SELECT event_type, COUNT(event.booking_id) AS total_tickets_sold
    FROM Event
    LEFT JOIN Booking ON Event.event_id = Booking.event_id
    GROUP BY event_type, Event.event_id
) AS subquery
GROUP BY event_type;


SELECT event_name
FROM Event
WHERE ticket_price > (SELECT AVG(ticket_price) FROM Event);


SELECT customer_name,
    (SELECT SUM(total_cost) FROM Booking WHERE Customer.customer_id = Booking.customer_id) AS total_revenue
FROM Customer;


SELECT customer_name
FROM Customer
WHERE customer_id IN (SELECT DISTINCT customer_id FROM Booking WHERE event_id IN (SELECT event_id FROM Event WHERE venue_id = 1));


SELECT event_type, SUM(total_tickets_sold) AS total_tickets_sold
FROM (
    SELECT event_type, COUNT(event.booking_id) AS total_tickets_sold
    FROM Event
    LEFT JOIN Booking ON Event.event_id = Booking.event_id
    GROUP BY event_type, Event.event_id
) AS subquery
GROUP BY event_type;

SELECT customer_name, DATE_FORMAT(booking_date, '%Y-%m') AS month
FROM Customer
JOIN Booking ON Customer.customer_id = Booking.customer_id
GROUP BY customer_name, month;



SELECT venue_id, AVG(ticket_price) AS average_ticket_price
FROM Event
WHERE venue_id IN (SELECT DISTINCT venue_id FROM Event)
GROUP BY venue_id;
