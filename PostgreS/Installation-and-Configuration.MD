### Installation and Service Configuration
Installation on CentOS 7:
 - **Install rpm repo to pull from the postgresql repo** : rpm -Uvh https://yum.postgresql.org/9.4/redhat/rhel-7-x86_64/pgdg-centos94-9.4-3.noarch.rpm
 - **Perform a system updateP** : yum update
 - **Install the server & contribution module** : yum install postgresql94-server posgresql94-contrib
 - **Initialize the database** : /usr/pgsql-9.4/bin/postgresql94-setup initdb
 - **enable service to start on boot** : systemctl enable postgresql-9.4

###### SE-Linux Config
In order to allow incoming connections from http this should be allowed through SElinux with the following command:
 - setsebool -P httpd_can_network_connect_db 1 
