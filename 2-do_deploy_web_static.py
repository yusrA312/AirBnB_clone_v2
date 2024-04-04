#!/usr/bin/python3
"""
archive to the web servers
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ["3.84.238.226", "54.84.245.120"]


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        f_n = archive_path.split("/")[-1]
        no_ext = f_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(f_n, path, no_ext))
        run('rm /tmp/{}'.format(f_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except Exception as e:
        return False
