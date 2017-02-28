-- create a SELECT statement, this SELECT statement will use an EXISTS to check
-- whether a department has had a sale with a price over 98.00 dollars.

-- departments table schema

-- id
-- name
-- sales table schema

-- id
-- department_id (department foreign key)
-- name
-- price
-- card_name
-- card_number
-- transaction_date
-- resultant table schema

-- id
-- name

-- Answer :
SELECT id, name FROM departments
WHERE EXISTS (SELECT 1 FROM sales WHERE sales.department_id = departments.id and price > 98)




-- Using only SQL, write a query that returns all rows in the custid, 
-- custname, and custstate columns from the customers table.

-- Table Description for customers:

-- Column	Data Type	Size	Sample
-- custid	integer	8	4
-- custname	string	50	Anakin Skywalker
-- custstate	string	50	Tatooine
-- custard	string	50	R2-D2
-- Your solution should contain only SQL.

-- Answer
SELECT custname, custid, custstate FROM customers



-- For this challenge you need to create a simple query to display
--  each unique clan with their total points and ranked by their total points.

-- people table schema

-- name
-- points
-- clan
-- You should then return a table that resembles below

-- select on

-- rank
-- clan
-- total_points
-- total_people
-- The query must rank each clan by their total_points, you must return each 
-- unqiue clan and if there is no clan name you must replace it with 
-- [no clan specified], you must sum the total_points for each clan and 
-- the total_people within that clan.

-- Note

-- The data is loaded from the live leaderboard, this means values will 
-- change but also could cause the kata to time out retreiving the information.

-- Answer
-- SELECT clan, COUNT (people.name) AS total_people, 
-- SUM (points) AS total_points FROM people
-- GROUP BY people.clan, people.name ORDER BY total_points desc


-- SELECT district, COUNT (employees.company_name) AS total_people, 
-- SUM (company_points) AS total_points FROM employees
-- GROUP BY employees.district, employees.company_name  ORDER BY total_points desc



-- SELECT (case clan WHEN null OR '' THEN 'NOT AVAILABLE' ELSE district) 
-- AS district, COUNT (employees.company_name) AS total_people, 
-- SUM (company_points) AS total_points FROM employees
-- GROUP BY employees.district, employees.company_name  ORDER BY total_points desc


-- SELECT clan = (case clan WHEN null OR '' THEN '[no clan specified]' ELSE clan) , 
-- COUNT (people.name) AS total_people, 
-- SUM (points) AS total_points FROM people
-- GROUP BY  people.clan, people.name ORDER BY total_points desc


-- SELECT clan, COUNT (people.name) AS total_people, 
-- SUM (points) AS total_points FROM people
-- GROUP BY people.clan, people.name ORDER BY total_points desc

-- SELECT clan, case WHEN clan = '' THEN '[no clan specified]' ELSE COUNT (people.name) AS total_people, 
-- SUM (points) AS total_points FROM people
-- GROUP BY  people.clan, people.name ORDER BY total_points desc



For this challenge you need to create a basic Age Calculator function
 which calculates the age in years on the age field of the peoples table.

The function should be called agecalculator, it needs to take 1
 date and calculate the age in years according to the date NOW and must return an integer.

You may query the people table while testing but the query
must only contain the function on your final submit.

people table schema

id
name
age

-- Answer
CREATE function agecalculator ()
RETURNS real AS $ages$
DECLARE
	ages real;
BEGIN
	SELECT age(timestamp 'NOW') into ages;
	RETURN ages;
END
$ages$
LANGUAGE plpgsql;

CREATE FUNCTION agecalculator(date varchar) returns varchar as $$
    select age(timestamp 'NOW');
$$ language 'sql';
