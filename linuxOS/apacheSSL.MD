# SSL Certificate on CentOS server Running Apache

This guide will demonstrate how to install and SSL certificate along with an existing Apache web server. Conventionally, one would normally pay for an SSL certificate and keep on renwing this certificate depending on the duration of the payment. 

This has all changed with [letsEncrypt](https://letsencrypt.org)

SSL Certificate Basics:

* It encrypts traffic between a web browser and web server
* It improves data security
* End users' trust is also increased with the use of SSL certs
* There is also SEO benefit, for example, Google ranks websites with SSL higher

## Requirements
* CentOS/RHEL server
* [Git](https://git-scm.com/downloads)
* [Vagrant](https://www.vagrantup.com/downloads.html)

## Steps
* Download [this folder]() to your computer and unzip it
* On your terminal change into the folder and run the following command
	- vagrant up:

* Install the Apache web server and mod ssl package which provides support to Apache:
	- yum install -y httpd mod_ssl
* Start the Apache web server and enbale to start up on boot:
	- systemctl start httpd; systemctl enable httpd  


Prior to installing the SSL certificate, the **certbot** application will be needed:

* yum install -y epel-release; yum install -y certbot

The certbot application has various plugins that are used for updating the configuration of web servers automatically.
Install the Apache plugin for certbot:

* yum install -y python2-certbot-apache.noarch

