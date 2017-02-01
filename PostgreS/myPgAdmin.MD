##### Installing and Configuring myPgAdmin
yum install -y phpPgAdmin


#### Accepting External Connections
modify the following files:
 - /etc/httpd/conf.d/phpPgAdmin.conf
 - /var/lib/pgsql/9.4/data/pg_hba.conf
 - /var/lib/pgsql/9.4/data/postgresql.conf

The restart the following services:
 - systemctl restart httpd
 - systemctl restart postgresql-9.4


#### Backing Up and Restoring Databases