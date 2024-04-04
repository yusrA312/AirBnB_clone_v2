# puppet
exec { 'apt-get-update':
  command => '/usr/bin/apt-get -y update',
  path    => '/usr/bin',
}

package { 'nginx':
  ensure => installed,
  require => Exec['apt-get-update'],
}

file { '/data/web_static/releases/test/':
  ensure => directory,
}

file { '/data/web_static/shared/':
  ensure => directory,
}

file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => 'Puppet x Holberton School',
}

file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
}

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  require => File['/data/web_static/current'],
  notify  => Exec['nginx-restart'],
  content => template('nginx/default_site.erb'),
}

exec { 'nginx-restart':
  command => '/usr/sbin/service nginx restart',
  path    => '/usr/bin',
  refreshonly => true,
}

exec { 'chown-data-directory':
  command => '/bin/chown -R ubuntu:ubuntu /data',
}
