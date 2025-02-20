#!/usr/bin/python3
"""fabric functions to work with development"""
from fabric.api import local, run, cd, sudo, put, get, env
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


def do_clean(number=0):
    """deletes out-of-date archive"""

    with cd("/data/web_static/releases/"):
        sudo("ls -t > del_files")

        get("/data/web_static/releases/del_files", "./del_files")

        with open('del_files', 'r') as file:
            list_file = file.read().strip().split('\n')
            if int(number) < 2:
                deleter = 1
            else:
                deleter = int(number)

            if len(list_file) > deleter:
                while deleter < len(list_file):
                    if not os.path.exists(list_file[deleter]):
                        continue
                    if not list_file[deleter].endswith('tgz'):
                        continue
                    try:
                        sudo(f"rm -rf {list_file[deleter]}")
                    except Exception:
                        sudo(f"rm -f {list_file[deleter]}")
                    deleter += 1

        sudo("rm -f del_files")

    local("ls -t versions > del_files")
    with open('del_files', 'r') as file:
        list_file = file.read().strip().split('\n')
        if int(number) < 2:
            deleter = 1
        else:
            deleter = int(number)

        if len(list_file) > deleter:
            while deleter < len(list_file):
                if not os.path.exists(list_file[deleter]):
                    continue
                try:
                    local(f"rm -f versions/{list_file[deleter]}")
                except Exception:
                    local(f"sudo rm -rf versions/{list_file[deleter]}")
                deleter += 1

    local("sudo rm -f del_files")
