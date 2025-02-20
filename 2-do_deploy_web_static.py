#!/usr/bin/python3
"""fabric functions to work with development"""
from fabric.api import local, run, put, env
from datetime import datetime
import os


env.hosts = ['3.94.86.136', '54.227.89.138']
env.user = 'ubuntu'


def do_pack():
    """generate archive file .tgz"""
    try:
        local("mkdir -p versions")
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = f'versions/web_static_{time}.tgz'
        local(f"tar cvfz {file_name} web_static")
        return file_name
    except Exception:
        return None


def do_deploy(archive_path):
    """deploy file to web servers"""
    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")
        file = archive_path.split('/')[-1]
        run(f'tar xzf /tmp/{file} -C /data/web_static/releases/')
        run(f"rm -f /tmp/{file}")
        run("rm -f /data/web_static/current")
        run(f"ln -sf /data/web_static/releases/\
            {file[:file.index('_', file.index('_') + 1)]} \
             /data/web_static/current")
        return True
    except Exception:
        return False
