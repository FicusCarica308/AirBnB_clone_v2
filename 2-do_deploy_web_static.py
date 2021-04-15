#!/usr/bin/python3
""" 2-do_deploy_web_static.py """
from datetime import datetime
import os
from fabric.api import run, env, put

env.hosts = ["35.185.53.142", "34.73.117.146"]

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

def do_deploy(archive_path):
    """TEMP DOC"""
    # returns false if file path does not exist
    if os.path.exists(archive_path) is False:
        return False

    # Isolates name of archive Ex. versions/web_static_344.tgz returns just web_static_344.tgz
    archive = archive_path.split('/')[1]
    # file name of archive without .tgz extension
    no_tgz = archive.split('.')[0]

    # puts archive into /tmp directory
    put(archive_path, "/tmp/{}".format(archive))
    
    # unpacks the archive into releases folder
    run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(archive, no_tgz)
    # web_static_20210415041759.tgz
    # removes archive from tmp directory
    run('rm /tmp/{}'.format(archive))
    run('rm /data/web_static/current')
    run('ln -s /data/web_static/releases/{} /data/web_static/current'.format(no_tgz))
