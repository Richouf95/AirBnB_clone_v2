#!/usr/bin/python3
"""
generates a .tgz archive from the contents of the web_static
"""


from datetime import datetime
from fabric.api import *


def do_pack():
    """
        make archive
    """
    time = datetime.now()
    archive_name = "web_static_{}.tgz".format(time.strftime("%Y%m%d%H%M%S"))
    local('mkdir -p versions')
    ziping = local('tar -cvzf versions/{} web_static'.format(archive_name))

    if ziping is not None:
        return archive_name
    else:
        return None
