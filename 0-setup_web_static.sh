#!/usr/bin/env bash
# setup nginx environment for deployment
if ! command nginx &> /dev/null; then
    sudo apt update
    sudo apt install -y nginx
fi
sudo mkdir -p /data/web_static/{releases/test,shared}
echo "It works!" | sudo tee -a /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/default.bak
sudo sed -i '0,/server_name _;/s//&\n   location \/hbnb_static\/ {\n        alias \/data\/web_static\/current\/; \n     }/' /etc/nginx/sites-available/default
sudo service nginx restart
