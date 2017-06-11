## Basic Apache HTTPD Configuration on RHEL7
A default configuration file is written to ``` /etc/httpd/conf/httpd.conf ``` post installation of the web-server package group or the httpd package group.

Contents of ``` /var/www/html ``` are served out by the configuration for requests coming in to any hostname over plain http.
The basic syntax of the ** httpd.conf ** file comprises 2 parts, namely ** Key Value ** configuration directives, as well as
** HTML-Like ** ** <Blockname parameter> ** blocks which in turn consists of other directives for configuration embedded in them.

Below are some of the important areas of the default configuration file