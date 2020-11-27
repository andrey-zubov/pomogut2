сертификаты:
https://gist.github.com/dancheskus/8d26823d0f5633e9dde63d150afb40b2

пути в init-letsencrypt.sh неправильные, правильные:
curl -s https://raw.githubusercontent.com/certbot/certbot/master/certbot-nginx/certbot_nginx/_internal/tls_configs/options-ssl-nginx.conf > "$data_path/conf/options-ssl-nginx.conf"
curl -s https://raw.githubusercontent.com/certbot/certbot/master/certbot/certbot/ssl-dhparams.pem > "$data_path/conf/ssl-dhparams.pem"

Если нужно создать сертефикаты - при запуксе ./init-letsencrypt.sh в nginx.conf закоментить listen 443 ssl и папки, кроме location /.well-known/acme-challenge/ { root /var/www/certbot; }
ПОсле создания сертефикатов - раскоментить.



