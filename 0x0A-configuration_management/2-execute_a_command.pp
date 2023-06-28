# creates a manifest that kills a process named killmenow

exec {'/usr/bin/pkill':
    command => '/bin/pkill -f killmenow'
}
