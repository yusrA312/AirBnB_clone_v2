#!/usr/bin/python3
"""
Fabric script
"""

from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """generates a tgz archive"""
    try:
        d_time = datetime.now()
    output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        d_time.year,
        d_time.month,
        d_time.day,
        d_time.hour,
        d_time.minute,
        d_time.second
    )
        if isdir("versions") is False:
            local("mkdir versions")
            file_name = "versions/web_static_{}.tgz".format(output)
            local("tar -cvzf {} web_static".format(file_name))
            return file_name
    except:
        return None

