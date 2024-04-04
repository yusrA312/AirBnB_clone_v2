#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric.api import put, run, env
from os.path import exists

env.hosts = ['142.44.167.228', '144.217.246.195']


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        no_extension = file_name.split(".")[0]
        path = "/data/web_static/releases/"

        put(archive_path, '/tmp/')
        run(f'mkdir -p {path}{no_extension}/')
        run(f'tar -xzf /tmp/{file_name} -C {path}{no_extension}/')
        run(f'rm /tmp/{file_name}')
        run(f'mv {path}{no_extension}/web_static/* {path}{no_extension}/')
        run(f'rm -rf {path}{no_extension}/web_static')
        run(f'rm -rf /data/web_static/current')
        run(f'ln -s {path}{no_extension}/ /data/web_static/current')
        
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
