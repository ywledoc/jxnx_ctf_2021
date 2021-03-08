FROM ctftraining/base_image_nginx_mysql_php_73

EXPOSE 80

COPY ./test_godzilla /var/www/html
COPY ./flag.sh /flag.sh

RUN /flag.sh && \
    rm -rf /flag.sh
