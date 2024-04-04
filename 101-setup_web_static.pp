# setup_web_static.pp

# Update package repositories and upgrade installed packages
exec { 'apt_update':
  command => '/usr/bin/apt-get update && /usr/bin/apt-get upgrade -y',
  path    => '/usr/bin',
}

# Install nginx
package { 'nginx':
  ensure => installed,
}

# Create directories
file { ['/data/web_static/releases/test', '/data/web_static/shared']:
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Create index.html file
file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => '<html><head></head><body>Holberton School</body></html>',
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

# Create symbolic link
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
}

# Configure nginx
file { '/etc/nginx/sites-enabled/default':
  ensure  => present,
  content => template('yourmodule/default.erb'), # You'll need to create a template for nginx configuration
  notify  => Service['nginx'],
}

# Restart nginx
service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  require    => File['/etc/nginx/sites-enabled/default'],
}
