#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""
from fabric.api import put, run, env
from os.path import exists

env.hosts = ['3.84.238.226', '54.84.245.120']
env.user = "ubuntu"
def do_deploy(archive_path):
    """Distributes an archive to the web servers."""
    if not exists(archive_path):
        return False
    
    try:
        file_name = archive_path[9:]
        no_extension = file_name.split(".")[0]
        remote_dir = "/data/web_static/releases/"
        
        # Upload archive to remote server
        put(archive_path, '/tmp/')
        
        # Create directory for the new version
        run('mkdir -p {}{}'.format(remote_dir, no_extension))
        
        # Extract archive to the new directory
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, remote_dir, no_extension))
        
        # Remove uploaded archive from /tmp/
        run('rm /tmp/{}'.format(file_name))
        
        # Move contents to parent directory
        run('mv {}{}/web_static/* {}{}/'.format(remote_dir, no_extension, remote_dir, no_extension))
        
        # Remove unnecessary directory
        run('rm -rf {}{}/web_static'.format(remote_dir, no_extension))
        
        # Update symbolic link
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(remote_dir, no_extension))
        
        return True
    except Exception as e:
        print("Exception:", e)
        return False
