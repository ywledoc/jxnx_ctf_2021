FROM ctftraining/base_image_nginx_mysql_php_73



ENV FLAG_TABLE=ctf_flag
ENV FLAG_COLUMN=f1ag


COPY ./src /var/www/html
COPY ./flag.sh /flag.sh

RUN chmod +x /flag.sh && \
    /flag.sh 
