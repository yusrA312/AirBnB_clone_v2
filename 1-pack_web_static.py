#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""

import datetime as dt
import subprocess
from fabric.api import local
from os.path import isdir


def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if not isdir("versions"):
            local("mkdir -p versions")
            current_datetime = dt.datetime.now().strftime("%Y%m%d%H%M%S")
            file_name = f"versions/web_static_{current_datetime}.tgz"
            subprocess.run(["tar", "-czvf", file_name, "web_static"])
        return file_name
    except Exception as e:
        print("An error occurred: {}".format(e))
        return None
