# Configuration Management for SSH authentication
include stdlib

file_line { 'Sets no passwd auth':
    ensure  => present,
    path    => '/etc/ssh/ssh_config',
    line    => 'PasswordAuthentication no',
    replace => true,
}

file_line { 'Sets the indentity file':
    ensure  => present,
    path    => '/etc/ssh/ssh_config',
    line    => 'IdentityFile ~/.ssh/school',
    replace => true,
}