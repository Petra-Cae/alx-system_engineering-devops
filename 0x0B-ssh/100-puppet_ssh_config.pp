#!/usr/bin/env bash
# Automates connection to a web server w/o a password

file { "/etc/ssh/ssh_config":
  ensure  => present,

content => "
    # SSH client configuration

    Host *
      PasswordAuthentication no
      IdentityFile ~/.ssh/school
  ",
}
