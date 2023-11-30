# Configuration Management for SSH authentication

file_line{'Sets no passwd auth':
    ensure  => present,
    path    => '/etc/ssh/sshd_config',
    line    => 'PasswordAuthentication no',
    replace => true,
}

file_line {'Sets the indentity file':
    ensure  => present,
    path    => '/etc/ssh/sshd_config',
    line    => 'IdentifyFile ~/.ssh/school',
    replace => true,
}