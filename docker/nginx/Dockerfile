FROM nginx

COPY SSL/privkey.pem /etc/letsencrypt/live/glocs.ru/privkey.pem

RUN rm /etc/nginx/conf.d/default.conf
COPY fullchain.pem /etc/letsencrypt/live/glocs.ru/fullchain.pem
COPY nginx.conf /etc/nginx/conf.d