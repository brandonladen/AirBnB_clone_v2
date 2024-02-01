#!/usr/bin/env bash
#A bash script that sets up web servers for the deployment of web_static
sudo apt -y update
sudo apt -y install nginx

#Create directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared/

#Create a fake HTML file
echo "<h1>Hello Africa!</h1>" | sudo dd status=none of=/data/web_static/releases/test/index.html

# create symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# give user ownership to directory
sudo chown -R ubuntu:ubuntu /data/

# backup default server config file
sudo cp /etc/nginx/sites-enabled/default nginx-sites-enabled_default.backup

# Set-up the content of /data/web_static/current/ to redirect
# to domain.tech/hbnb_static
sudo sed -i '37i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

sudo service nginx restart
