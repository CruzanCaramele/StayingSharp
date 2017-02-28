#### Creating Databases
To create a database "mytestdb" run the following commands:
 - su - postgres
 - createdb mytestdb

To connect to the database "mytestdb" run the following:
 - \connect mytestdb
   You are now connected to database "mytestdb" as user "postgres".

#### Creating Tables
To create a table within the "mytestdb" database, run the following command:
 - mytestdb=# CREATE TABLE cities (
   mytestdb(# cityid varchar(5),
   mytestdb(# cityname varchar(80),
   mytestdb(# state varchar(20) );
   **CREATE TABLE**


To insert values into the table "cities":
 - mytestdb=# INSERT INTO cities VALUES (
   mytestdb(# 12345,
   mytestdb(# 'Cincinnati',
   mytestdb(# 'Ohio');
   **INSERT 0 1**


mytestdb=# SELECT * FROM cities;
 cityid |  cityname  | state
--------+------------+-------
 12345  | Cincinnati | Ohio
(1 row)



#### Roles - Creating and Deleting Users
To create a user and set a password for the user, run the following commands:
 - su - postgres
 - createuser test
 - createdb testuser
 - psql 
 - ALTER USER test WITH PASSWORD 'password'; (from the psql client)

To login as the user "test", run:
 - psql -U test

To allow password login for the users alter the /var/lib/pgsql/9.4/data/pg_hba.conf file.
Allow password login for IPv4 or IPv6 and also for the Unix Domain socket.


#### Roles - Assigning Permissions
Assuming a new user called "tester" has been created and a new database called
newdb is also created with a table "tbltest"
To grant permission to the user "tester" to INSERT into tables , run the following:
 - GRANT INSERT on tbltest TO tester;
 - GRANT ALL on tbltest TO tester;

To Revoke roles:
 - REVOKE



#### Backing Up and Restoring Databases
- connect to the database to be backed up
  - \connect dbtest
- check or add values as needed and quit out of the database
  - pg_dump dbtest > dbtest.txt
- to restore the data back into the database
  - psql dbtest < dbtest.txt

#### Replication - Master Server Configuration
- navigate to cd /var/lib/pgsql/9.4/data & and make changes to the postgresql.conf file
  - set **wal_level** to **hot_standby**
  - set the number of slaves by changing **max_wal_senders = 1** . In this case 1 slave only
  - set the standby server names **synchronous_standby_names = 'zaria3'**
  - connect to psql and a database, then create a user for replication:
    - create user replica replication;
  - add the following line at the end of /var/lib/pgsql/9.4/data/pg_hba.conf
    - host     replication     replica         SLAVE_SERVER_IP_ADDRESS          trust


#### Replication - Slave Server Configuration
- on the slave server, stop the postgresql service
- delete all data in /var/lib/pgsql/9.4/data 
- run pgsql:
  - pg_basebackup -D /var/lib/pgsql/9.4/data/ -h MASTER_SERVER_IP_ADDRESS -U replica