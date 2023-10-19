# enable Holberton user to login and open files

# increase hard file limit
exec { 'Holberton-user-hard-file-limit':
  command => "sed -i '/^holberton hard/s/5/30000/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/',
}

# increase soft file limit
exec { 'Holberton-user-soft-file-limit':
  command => "sed -i '/^holberton soft/s/4/20000/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/',
}
