# This manifest handles the task of creating a custom HTTP header response
# does not setup server like task 0 just the custom header !!!!
exec {'Install nginx':
    path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
    command => 'sudo apt-get -y update; sudo apt-get -y install nginx'
}
exec {'mkdirectorys':
    path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
    command => 'mkdir -p /data/web_static/releases/test/; mkdir -p /data/web_static/shared/'
    require => Exec['Install nginx'],
}
file {'create index.html':
  path    => '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>'
  ensure  => 'present',
  mode    => '0664',
  content => 'I love Puppet',
  require => Exec['mkdirectorys'],
}
exec {'rm/ln':
    path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
    command => 'rm -f /data/web_static/current;
    ln -s /data/web_static/releases/test/ /data/web_static/current;
    sudo chown -R ubuntu:ubuntu /data/;
    sudo sed -i "/listen \[::\]:80 default_server/a location /hbnb_static {\n\talias /data/web_static/current/;\n" /etc/nginx/sites-available/default
    sudo service nginx restart
    '
}
