# Puppet script to create a custom HTTP heaser response

exec { 'command':
  command  => 'sudo apt-get -y update;
           apt-get install -y nginx;
           sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
           service nginx restart',
  provider => shell,
}
