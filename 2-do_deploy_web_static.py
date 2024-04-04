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
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run(f"mkdir -p {path}{no_ext}/")
        run(f"tar -xzf /tmp/{file_n} -C {path}{no_ext}/")
        run(f"rm /tmp/{file_n}")
        run(f"mv {path}{no_ext}/web_static/* {path}{no_ext}/")
        run(f"rm -rf {path}{no_ext}/web_static")
        run("sudo rm -rf /data/web_static/current")
        run(f"sudo ln -s {path}{no_ext}/ /data/web_static/current")
        return True
    except:
        return False
