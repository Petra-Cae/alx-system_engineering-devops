# installs an Nginx server with a few configuration changes

package { 'nginx':
  ensure  => 'present',
}

# install updates
exec { 'update':
  command   => 'sudo apt-get update',
  provider  => 'shell',
}

# install nginx
exec { 'install':
  command   =>  'sudo apt-get install nginx -y',
  provider  =>  'shell',
}

# change folder rights cautiously
exec { 'rights':
  command   =>  'sudo chmod -R 755',
  path      =>  '/etc/nginx',
  provider  =>  'shell',
}

# change index message
exec { 'greet':
   command   => 'echo "Hello World!" > /etc/nginx/html/index.html',
   provider  => 'shell',
}

# redirection
exec { 'redirect':
  command   => '/usr/bin/sudo /bin/sed -i "66i rewrite ^/redirect_me https://www.youtube.com/ permanent;" /etc/nginx/sites-available/default',
  provider  => 'shell',
}

# restart Nginx
exec { 'restart':
    command   => 'sudo service nginx restart',
    provider  => 'shell',
}
