Here's just a sampling of the many data types that SQL supports. We won't be using most of these types in this course, though.

The exact list of types differs from one database to another. For a full list of types, check the manual for your database, such as [this one for PostgreSQL](https://www.postgresql.org/docs/9.4/static/datatype.html).

Text and string types
text — a string of any length, like Python str or unicode types.
char(n) — a string of exactly n characters.
varchar(n) — a string of up to n characters.

Numeric types
integer — an integer value, like Python int.
real — a floating-point value, like Python float. Accurate up to six decimal places.
double precision — a higher-precision floating-point value. Accurate up to 15 decimal places.
decimal — an exact decimal value.

Date and time types
date — a calendar date; including year, month, and day.
time — a time of day.
timestamp — a date and time together.