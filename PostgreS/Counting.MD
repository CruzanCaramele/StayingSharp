#### Counting what isn’t there
Counting rows in a single table is something you’ve seen many times before in this course. A column aggregated with the count aggregation function will return the number of rows in the table, or the number of rows for each value of a group by clause.

For instance, you saw queries like these back in Lesson 2:

select count(*) from animals;
-- returns the number of animals in the zoo

select count(*) from animals where species = ‘gorilla’;
-- returns the number of gorillas

select species, count(*) from animals group by species;
-- returns each species’ name and the number of animals of that species

Things get a little more complicated if you want to count the results of a join. Consider these tables we saw earlier in Lesson 4, the products and sales tables for a store:

Products and Sales

Suppose that we want to know how many times we have sold each product. In other words, for each sku value in the products table, we want to know the number of times it occurs in the sales table. We might start out with a query like this:

select products.name, products.sku, count(*) as num
  from products join sales
    on products.sku = sales.sku
  group by products.sku;
But this query might not do exactly what we want. If a particular sku has never been sold — if there are no entries for it in the sales table — then this query will not return a row for it at all.

If we wanted to see a row with the number zero in it, we’ll be disappointed!

However, there is a way to get the database to give us a count with a zero in it. To do this, we’ll need to change two things about this query —

select products.name, products.sku, count(sales.sku) as num
  from products left join sales
    on products.sku = sales.sku
  group by products.sku;
This query will give us a row for every product in the products table, even the ones that have no sales in the sales table.

What’s changed? First, we’re using count(sales.sku) instead of count(*). This means that the database will count only rows where sales.sku is defined, instead of all rows.

Second, we’re using a left join instead of a plain join.

Um, so what’s a left join?
SQL supports a number of variations on the theme of joins. The kind of join that you have seen earlier in this course is called an inner join, and it is the most common kind of join — so common that SQL doesn’t actually make us say "inner join" to do one.

But the second most common is the left join, and its mirror-image partner, the right join. The words “left” and “right” refer to the tables to the left and right of the join operator. (Above, the left table is products and the right table is sales.)

A regular (inner) join returns only those rows where the two tables have entries matching the join condition. A left join returns all those rows, plus the rows where the left table has an entry but the right table doesn’t. And a right join does the same but for the right table.

(Just as “join” is short for “inner join”, so too is “left join” actually short for “left outer join”. But SQL lets us just say “left join”, which is a lot less typing. So we’ll do that.)