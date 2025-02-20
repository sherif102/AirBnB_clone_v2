#!/usr/bin/python3
"""fabric functions to work with development"""
from fabric.api import local, run, cd, sudo, put, lcd, env
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

    if int(number) == 0:
        number = 1
    else:
        number = int(number)

    with cd("/data/web_static/releases"):
        file_list = sudo("ls -tr").split()
        file_list = [x for x in file_list if "web_static_" in x]
        if len(file_list) > 0:
            [file_list.pop() for i in range(number)]
            [run("rm -rf ./{}".format(a)) for a in file_list]


    file_list = sorted(os.listdir("versions"))
    [file_list.pop() for i in range(number)]
    if len(file_list) > 0:
        [local("rm ./versions/{}".format(x)) for x in file_list]
