#!/usr/bin/python3
"""fabfile that compreses file for deployment"""
from fabric.api import local
from datetime import datetime


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
