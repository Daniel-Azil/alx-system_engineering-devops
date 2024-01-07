exec { 'add nginx stable dir repo':
  command => 'sudo add-apt-repository ppa:nginx/stable',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# update software packages list
exec { 'updates package':
  command => 'apt-get update',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

package { 'nginx':
  ensure     => 'installed',
}

exec { 'execute HTTP file':
  command => "ufw allow 'Nginx HTTP'",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  onlyif  => '! dpkg -l nginx | egrep \'îi.*nginx\' > /dev/null 2>&1',
}

exec { 'change permission and mode':
  command => 'chmod -R 755 /var/www',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

file { '/var/www/html/index.html':
  content => "Hello World!\n",
}

file { '/var/www/html/404.html':
  content => "Ceci n'est pas une page\n",
}

file { 'CM for Nginx':
  ensure  => file,
  path    => '/etc/nginx/sites-enabled/default',
  content =>
"server {
        listen 80 default_server;
        listen [::]:80 default_server;
               root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
        server_name _;
        location / {
                try_files \$uri \$uri/ =404;
        }
        error_page 404 /404.html;
        location  /404.html {
            internal;
        }
        
        if (\$request_filename ~ redirect_me){
            rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
        }
}
",
}

exec { 'restarts the server':
  command => 'service nginx restart',
  path    => '/usr/bin:/usr/sbin:/bin',
}

service { 'service is running':
  ensure  => running,
  require => Package['nginx'],
}