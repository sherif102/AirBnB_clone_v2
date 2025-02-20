#!/usr/bin/python3


def do_deploy(filing="/home/sheriff/versions/web_static_20170315003959.tgz"):
    """deploy file to web servers"""

    file = filing.split('/')[-1]
    print(file)
    print(file[:file.index('_', file.index('_') + 1)])

do_deploy()