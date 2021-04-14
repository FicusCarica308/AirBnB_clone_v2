#!/usr/bin/env bash
# Temp comment
file_path="/etc/nginx/sites-available/default"
fake_html="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"
listen="location /hbnb_static {\n\talias /data/web_static/current/;\n}"
# checks if nginx is installed using dpkg then installs if not
dpkg -s nginx &> /dev/null
if [ $? -ne 0 ]; then
    sudo apt-get -y update
    sudo apt-get -y install nginx
fi

# makes directorys using mkdir -p
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# creates a fake html
echo "$fake_html" > /data/web_static/releases/test/index.html

# creates symbolic link named /data/web_static/current to the folder /data/web_static/releases/test/
rm -f /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current

# adds group and user permissions to the /data/ dir recursivly
sudo chown -R ubuntu:ubuntu /data/

# adds serving of content /data/web_static/current/  to /hbnb_static/ domain dir  (ex: https://mydomainname.tech/hbnb_static).
sudo sed -i "/listen \[::\]:80 default_server/a $listen" $file_path
sudo service nginx restart