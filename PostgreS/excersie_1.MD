TE: These exercises can be completed on Linux Academy Lab Servers runniing CentOS 7 and logged in as the root user.
1. Find the PostgreSQL 9.4 repository RPM from the appropriate website and either download and install it using the appropriate package management commands or install directly from the website link.
  - Ans : rpm -Uvh https://yum.postgresql.org/9.4/redhat/rhel-7-x86_64/pgdg-centos94-9.4-3.noarch.rpm
          
2. Update your system after installing the repository update in Step #1, applying any necessary updates.
  - Ans : yum update -y

3. Using the appropriate package management command, install the PostgreSQL 9.4 server and associated contribed modules and utilities. Once installed, run the database initialization routine before starting the database.
  - Ans : yum install -y postgresql94-server postgresql94-contrib

4. Using the appropriate SYSTEMD service management commands, enable the PostgreSQL 9.4 server to run on system start and then start the database server.
  - Ans : systemctl enable postgresql-9.4

5. Check to see if SELinux is being run in enforced mode on your system. If so, run the command to allow external HTTP DB connections to the server through SELinux configuration.
  - Ans : **sestatus** to check the selinux status
          setsebool -P httpd_can_network_db 1

6. Become the 'postgres' user and run the 'psql' command. Once at the database prompt, set a password for the 'psql' user.
 - Ans : su - postgres
         psql
	 \password postgres  ( set the password and run \q to quit)

