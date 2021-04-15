#!/usr/bin/python3
""" 1-pack_web_static.py """
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    Description:
    A Fabric function that generates a .tgz archive
    from the contents of the web_static folder
    """
    time_name = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    try:
        local("tar -cvzf versions/web_static_{}.tgz web_static"
              .format(time_name))
    except:
        return None
    return "versions/web_static_{}.tgz web_static".format(time_name)
