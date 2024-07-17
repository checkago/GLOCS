FROM nginx

COPY privkey.pem /etc/letsencrypt/live/glocs.ru/privkey.pem
COPY fullchain.pem /etc/letsencrypt/live/glocs.ru/fullchain.pem
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d