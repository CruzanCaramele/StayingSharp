-- This contains a friends 
-- table and data will be added and deleted from it.

-- The instructions provided are a general guideline, but feel free to add more columns, 
-- insert more data, or create more tables.


-- Setup

-- 1.
-- Create a table named friends with the following columns: id, name, and birthday
-- 2.
-- Add Jane Doe to friends. Her birthday is May 19th, 1993.
-- 3.
-- Add three more of your friends to friends.
-- 4.
-- Jane Doe just got married! Her new last name is Smith. Update her record in your database.
-- 5.
-- Add a new column to your table named email.
-- 6.
-- Update the email address for each friend in your table. Jane Doe's email is jdoe@example.com.
-- 7.
-- Jane Doe is not a real person. Remove her from friends.
CREATE TABLE friends (
  id INTEGER,
  name TEXT,
  birthday DATE
);

INSERT INTO friends (
  id,
  name,
  birthday
) VALUES (
  1,
  'Jane Doe',
  05/19/1993
);

INSERT INTO friends (
  id,
  name,
  birthday
) VALUES (
  2,
  'Jonathan Doe',
  05/20/1993
);

INSERT INTO friends (
  id,
  name,
  birthday
) VALUES (
  3,
  'Ross Gellar',
  05/21/1993
);

INSERT INTO friends (
  id,
  name,
  birthday
) VALUES (
  4,
  'Rachel Green',
  05/23/1993
);

UPDATE friends
SET name = "Jane Smith"
WHERE id = 1;

ALTER TABLE friends
ADD COLUMN email;

UPDATE friends
SET email = 'jdoe@example.com'
WHERE id = 1;

UPDATE friends
SET email = 'jsddoe@example.com'
WHERE id = 2;

UPDATE friends
SET email = 'jdoer@example.com'
WHERE id = 3;

UPDATE friends
SET email = 'jrwdoe@example.com'
WHERE id = 4;

DELETE FROM friends
WHERE id = 1;