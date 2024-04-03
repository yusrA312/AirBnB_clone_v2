#!/usr/bin/env bash
# sets up web servers 
sudo apt-get update && sudo apt-get upgrade
sudo apt-get -y install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
cat << EOF | tee /data/web_static/releases/test/index.html
<html>
<head>
</head>
<body>
Holberton School
</body>
</html>
EOF

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu /data/
chgrp -R ubuntu /data/

sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

sudo service nginx restart
