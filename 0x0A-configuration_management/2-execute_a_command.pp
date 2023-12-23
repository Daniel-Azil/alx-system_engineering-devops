# Utilize Puppet's exec resource to create a manifest that
# terminates a process named 'killmenow' using the pkill command.

exec {'pkill':
  command  => 'pkill killmenow',
  provider => 'shell'
}
