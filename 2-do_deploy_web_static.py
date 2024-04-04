#!/usr/bin/python3
"""
Fabric script that distributes an archive to the web servers
"""

from fabric.api import put, run, env
from os.path import exists

env.hosts =  ['3.84.238.226', '54.84.245.120']


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_name = archive_path.split("/")[-1]
        file_name_no_ext = file_name.split(".")[0]
        releases_path = "/data/web_static/releases/"
        tmp_path = "/tmp/"
        put(archive_path, tmp_path)
        run(f'mkdir -p {releases_path}{file_name_no_ext}/')
        run(f'tar -xzf {tmp_path}{file_name} -C {releases_path}{file_name_no_ext}/')
        run(f'rm {tmp_path}{file_name}')
        run(f'mv {releases_path}{file_name_no_ext}/web_static/* {releases_path}{file_name_no_ext}/')
        run(f'rm -rf {releases_path}{file_name_no_ext}/web_static')
        run('rm -rf /data/web_static/current')
        run(f'ln -s {releases_path}{file_name_no_ext}/ /data/web_static/current')

        return True
    except:
        return False
