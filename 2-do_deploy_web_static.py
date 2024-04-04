#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""

from datetime import datetime
from fabric.api import local, put, run
from os.path import isdir
import os

env.hosts = ["3.84.238.226", "54.84.245.120"]
env.user = "ubuntu"

def do_pack():
    """
    Generates a tgz archive in the web_static folder
    """
    try:
        current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
        if not isdir("versions"):
            local("mkdir -p versions")
        file_name = "versions/web_static_{}.tgz".format(current_datetime)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("An error occurred:", e)
        return None


def do_deploy(archive_path):
    """
    Distribute archive.
    """
    if not os.path.exists(archive_path):
        return False
    
    archived_file = archive_path[9:]
    newest_version = f"/data/web_static/releases/{archived_file[:-4]}"
    archived_file = f"/tmp/{archived_file}"
    put(archive_path, "/tmp/")
    run(f"sudo mkdir -p {newest_version}")
    run(f"sudo tar -xzf {archived_file} -C {newest_version}/")
    run(f"sudo rm {archived_file}")
    run(f"sudo mv {newest_version}/web_static/* {newest_version}")
    run(f"sudo rm -rf {newest_version}/web_static")
    run(f"sudo rm -rf /data/web_static/current")
    run(f"sudo ln -s {newest_version} /data/web_static/current")

    return True
