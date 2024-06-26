#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""

from datetime import datetime
from fabric.api import local
from os.path import isdir


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


if __name__ == "__main__":
    do_pack()
