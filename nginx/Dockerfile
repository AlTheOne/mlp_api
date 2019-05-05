FROM nginx:latest

ADD nginx.conf /etc/nginx/nginx.conf
RUN chown -R nginx:nginx /dev/stdout

RUN mkdir -p /mlp_api/media
RUN mkdir -p /mlp_api/static

WORKDIR /mlp_api/media
RUN chown -R nginx:nginx /mlp_api/media

WORKDIR /mlp_api/static
RUN chown -R nginx:nginx /mlp_api/static