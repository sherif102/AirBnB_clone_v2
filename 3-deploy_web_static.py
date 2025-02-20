#!/usr/bin/python3
"""fabric functions to work with development"""
from fabric.api import local, run, sudo, put, env
from datetime import datetime
import os


env.hosts = ['3.94.86.136', '54.227.89.138']
env.user = "ubuntu"


def do_remove(file):
    """remove provided file/directory"""
    try:
        sudo(f"rm -rf {file}")
        return True
    except Exception:
        print("execution failed!")
        return False


def do_execute(file):
    """execute suplied file"""
    try:
        run(f"./{file}")
        return True
    except Exception:
        print("execution failed!")
        return False


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
        sudo(f'tar xzf /tmp/{file} -C /data/web_static/releases/')
        sudo(f"rm -f /tmp/{file}")
        sudo("rm -rf /data/web_static/current")
        sudo(f"ln -sf /data/web_static/releases/"
             f"{file[:file.index('_', file.index('_') + 1)]}"
             f" /data/web_static/current")
        return True
    except Exception:
        return False


def deploy():
    """create and deploy files to web_servers"""
    file = do_pack()
    if not file:
        return None
    result = do_deploy(file)
    return result
