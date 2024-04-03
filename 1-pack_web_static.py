#!/usr/bin/python3
"""
A module for Fabric script that generates a .tgz archive.
"""
from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """
    Generates a tgz archive in the web_static folder
    """
    try:
        YD= datetime.now().strftime("%Y%m%d%H%M%S")
        if not isdir("versions") :
            local("mkdir versions")
        ak= "versions/web_static_{}.tgz".format(YD)
        local("tar -cvzf {} web_static".format(ak))
        return ak
    except:
        return None


if __name__ == "__main__":
    do_pack()

