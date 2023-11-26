# A CM that ensures the installation of Flask version
# 2.1.0 using Puppet's package resource for pip3.

package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
