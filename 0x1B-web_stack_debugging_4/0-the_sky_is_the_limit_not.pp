# increase Nginx server traffic by upping the limit

# increase ULIMIT
exec { 'Nginx-fix':
  command  => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  path     => '/usr/local/bin/:/bin/',
}

# Nginx restart
exec { 'restart-Nginx':
  command  => '/etc/init.d/nginx restart',
  path     => '/etc/init.d',
}
