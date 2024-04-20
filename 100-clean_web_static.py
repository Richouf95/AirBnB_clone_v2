#!/usr/bin/python3
"""
generates a .tgz archive from the contents of the web_static
"""


from datetime import datetime
from fabric.api import *
from os.path import exists, isdir
import os
env.hosts = ['34.232.66.220', '35.153.193.79']


def do_pack():
    """
        make archive
    """
    try:
        if isdir("versions") is False:
            local("mkdir versions")
        archive_name = "versions/web_static_{}.tgz".format(
                datetime.now().strftime("%Y%m%d%H%M%S")
                )
        local('tar -cvzf {} web_static'.format(archive_name))
        return archive_name
    except Exception as e:
        print("Exception :", e)
        return None


def do_deploy(archive_path):
    """
        Deploye the web static
    """
    if exists(archive_path) is False:
        return False

    try:
        archive = archive_path.split('/')[-1].split('.')[0]
        remote_path = "/data/web_static/releases/"
        put(archive_path, '/tmp')
        run('mkdir -p {}{}/'.format(remote_path, archive))
        run('tar -xzf /tmp/{} -C {}{}/'.format(
            archive_path.split("/")[-1],
            remote_path,
            archive
            ))
        run('rm /tmp/{}'.format(archive_path.split("/")[-1]))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(remote_path, archive))
        run('rm -rf {}{}/web_static'.format(remote_path, archive))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(
            remote_path, archive
            ))

        return True
    except Exception as e:
        print("An error occurred:", e)
        return False


def deploy():
    """
        zip web static files and deploy it
    """
    archive = do_pack()

    if archive is None:
        return False

    return do_deploy(archive)


def do_clean(number=0):
    """Delete out-of-date archives.
    Args:
        number (int): The number of archives to keep.
    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
