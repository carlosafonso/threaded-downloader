FROM ubuntu/nginx:1.24-23.10_beta

RUN mkdir -p /var/www/html/data /var/www/html/upload
RUN head -c 10M /dev/urandom > /var/www/html/data/data_10m.bin
RUN head -c 100M /dev/urandom > /var/www/html/data/data_100m.bin
RUN head -c 1G /dev/urandom > /var/www/html/data/data_1g.bin
RUN touch /var/www/html/upload/index.html

COPY default /etc/nginx/sites-available/default
