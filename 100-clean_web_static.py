#!/usr/bin/python3
""" 3-deploy_web_static.py """
from datetime import datetime
import os
from fabric.api import run, env, put, local, lcd, cd


env.hosts = ["35.185.53.142", "34.73.117.146"]
local_check = 0

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
    return "versions/web_static_{}.tgz".format(time_name)


def do_deploy(archive_path):
    """
    Description:
    distributes an archive to your web servers
    Returns: returns false if a command fails / path is non existent

    Extra: used try / except instead of result.success
    since there would be to many checks / assignemtns
    """
    # returns false if path does not work
    if os.path.exists(archive_path) is False:
        print("jere")
        return False
    # creation of directory path we will unpack our archive into
    archive = archive_path.split('/')[1]
    no_tgz = archive.split('.')[0]
    unpack_dir = '/data/web_static/releases/{}/'.format(archive, no_tgz)

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/{}".format(archive))
        # Uncompress the archive to unpack_dir on the web server
        run("mkdir -p {}".format(unpack_dir))
        run("tar -xzf /tmp/{} -C {}".format(archive, unpack_dir))
        # Deletes the archive from the web server
        run("rm /tmp/{}".format(archive))
        # moves contents of unpackaging into the unpacked directory
        run("mv {}web_static/* {}".format(unpack_dir, unpack_dir))
        # removes directory we copy the contents from (not needed anymore)
        run("rm -rf {}web_static/".format(unpack_dir))
        # deletes and recreates symbo link /current leading it too unpack_dir
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(unpack_dir))
    except:
        return False
    return True


def deploy():
    """
    Description:
    creates and distributes an archive to your web servers using do_deploy()
    and do_pack()
    """
    path = do_pack()
    if path is None:
        return False
    value = do_deploy(path)
    return value


def do_clean(number=0):
    """
    Description:
        Deletes out-of-date archives
    Args:
       number(int): number is the number of the archives,
       including the most recent, to keep.
    If number is 0 or 1, keep only the most recent version
    of your archive. If number is 2, keep the most recent,
     and second most recent versions of your archive.
    """
    global local_check

    if int(number) == 0:  # if number is zero make it one
        number = 1

    if local_check == 0:
        with lcd('versions'):
            output = local("ls -1tr | grep -c .tgz", capture=True)
            number_delete = int(output) - int(number)
            local("ls -1tr | grep .tgz | head -n {} | xargs rm -f".format(number_delete))
        local_check += 1
        # deleting the wrong amount (when number is 1 deletes one instead of the rest)
    # with cd('/data/web_static/releases'):
        # run("ls -1tr | grep .tgz | head -n {} | xargs rm -rf".format(number))
    # ls -1tr | head -n 1 | xargs rm
