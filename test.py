#!/usr/bin/python3
"""fabric functions to work with development"""

with open('files', 'r') as file:
    file = file.read()
    flist = file.split('\n')
    print(flist)