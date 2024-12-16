mkdir -p nginx/ssl
cd nginx/ssl
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout server.key -out server.crt \
  -subj "/C=PT/ST=Algarve/L=Faro/O=ETICALGARVE/OU=ITDept/CN=localhost"