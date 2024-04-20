#!/usr/bin/env bash
# seting up web servers for web_static deployment

# install Nginx
sudo apt-get update
sudo apt-get -y install nginx

# Let Firewall allow Nginx http
sudo ufw allow 'Nginx HTTP'

# Create folders & file structure
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html

# Create index file in test with basic html code
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create symbolique link
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

# change owner
sudo chown -R ubuntu:ubuntu /data/

# Create alias
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# restart nginx
sudo service nginx restart
