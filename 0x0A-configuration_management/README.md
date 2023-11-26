# 0x0A Configuration Management

## Puppet Manifests

### 0-create_a_file.pp
```puppet
# A CM file that creates a file in the /tmp directory using Puppet.
file {'/tmp/school':
  ensure  => file,
  content => 'I love Puppet',
  path    => '/tmp/school',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data'
}
### 1-install_a_package.pp
# A CM that ensures the installation of Flask version
# 2.1.0 using Puppet's package resource for pip3.
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
### 2-execute_a_command.pp
# Utilize Puppet's exec resource to create a manifest that
# terminates a process named 'killmenow' using the pkill command.
exec {'pkill':
  command  => 'pkill killmenow',
  provider => 'shell'
}

