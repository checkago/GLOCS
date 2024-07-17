FROM nginx

COPY fullchain.pem /etc/letsencrypt/live/glocs.ru/fullchain.pem
COPY privkey1.pem /etc/letsencrypt/live/glocs.ru/privkey.pem
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d