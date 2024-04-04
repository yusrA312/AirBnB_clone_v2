#!/usr/bin/python3
"""
an archive
"""

from datetime import datetime
from fabric.api import *
import os

env.hosts = ["3.84.238.226", "54.84.245.120"]
env.user = "ubuntu"


def do_deploy(archive_path):
    """
        Distribute archive.
    """
    if os.path.exists(archive_path):
        archived_file = archive_path[9:]
        newest_version = "/data/web_static/releases/" + archived_file[:-4]
        archived_file = "/tmp/" + archived_file
        put(archive_path, "/tmp/")
        run(f"sudo mkdir -p {newest_version}")
        run(f"sudo tar -xzf {archived_file} -C {newest_version}/")
        run(f"sudo rm {archived_file}")
        run(f"sudo mv {newest_version}/web_static/* {newest_version}")
        run(f"sudo rm -rf {newest_version}/web_static")
        run(f"sudo rm -rf /data/web_static/current")
        run(f"sudo ln -s {newest_version} /data/web_static/current")
        return True

    return False

if __name__ == "__main__":
    do_deploy(archive_path)
