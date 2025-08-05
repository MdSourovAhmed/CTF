FROM php:8.2-apache  

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    apt-get install -y \
    gcc \ 
    libbz2-dev && \
    docker-php-ext-install bz2 && \
    rm -rf /var/lib/apt/lists/

RUN rm -rf /var/www/html/*

COPY flag.txt readflag.c /
RUN gcc -o /readflag /readflag.c && \
    rm /readflag.c

RUN chown 0:1337 /flag.txt /readflag && \
    chmod 040 /flag.txt && \
    chmod 2555 /readflag

COPY src/index.php src/upload.php /var/www/html/

RUN chown -R root:root /var/www && \
    find /var/www -type d -exec chmod 555 {} \; && \
    find /var/www -type f -exec chmod 444 {} \; && \
    mkdir /var/www/html/uploads && \
    chmod 703 /var/www/html/uploads

RUN find / -ignore_readdir_race -type f \( -perm -4000 -o -perm -2000 \) -not -wholename /readflag -delete
USER www-data
RUN (find --version && id --version && sed --version && grep --version) > /dev/null
USER root

EXPOSE 80
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
