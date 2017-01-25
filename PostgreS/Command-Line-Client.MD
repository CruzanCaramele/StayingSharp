#### Command Line
By default a postgres user is created upon installation as **postgres**.
To switch to the user and enter into the postgres interactive shell and set a password for the user:
 - su - postgres
 - bash-4.2$ psql
     psql (9.4.10)
     Type "help" for help.
 - postgres=# \password postgres


##### Create Extension pack
It's useful to create an extension to include semi-colon at the end of each query. It can be done with the following command within the postgresql shell:
 - CREATE EXTENSION adminpack;
