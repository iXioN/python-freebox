# !/usr/bin/env python
# -*- coding: utf-8 -*-
#  freebox.py
#  python-freebox
#  
#  Created by antonin on 2013-03-29.
#  Copyright 2013 antonin. All rights reserved.
# 
"""Usage:
  freebox.py client [--host=HOST][--port=PORT][--password=PASSWORD]
  freebox.py download [--host=HOST][--port=PORT][--password=PASSWORD] PATH_OR_URL
  freebox.py -h | --help | --version
  
  Options:
    --help                  Show this screen.
    -v --version            Show version.
    -h --host=HOST>         freebox host [default: mafreebox.free.fr].
    -p --port=PORT          freebox port [default: 80].
    -w --password=PASSWORD  freebox password .
"""
#futur usage    freebox.py download <file>
#               freebox.py download -l | --list


#see
#http://www.chosesafaire.fr/2012/05/api-minimaliste-freebox-revolution/
#https://github.com/fdev31/pyFreebox/tree/master/freebox
#http://www.freebox-v6.fr/wiki/index.php?title=API#Transmission

#torrent link : http://cdimage.debian.org/debian-cd/6.0.7/amd64/bt-cd/debian-6.0.7-amd64-netinst.iso.torrent
#personal ip = "88.164.113.16:8000"
import sys
import os
import urlparse
from docopt import docopt 
from getpass import getpass
from client import freeboxClient
from download import Downloader


def main():
    # parser = OptionParser(usage="usage: %prog filename",
    #                      version="%prog 0.1")
    # parser.add_option("-i", "--freeboxip", dest="freebox_ip",
    #          help="the freebox ip addr", metavar="freebox_ip", default="")
    # parser.add_option("-f", "--file", dest="torrent_file",
    #          help="the torrent file to download", metavar=".torrent", default="")
    # parser.add_option("-u", "--url", dest="url_to_download",
    #            help="the http or magnet url", metavar="url", default="")
    #  
    # (options, args) = parser.parse_args()
    
    arguments = docopt(__doc__, version='0.1.1-dev') #TODO get the version from __init__.py
    
    host = arguments.get('--host', 'mafreebox.free.fr')
    port = arguments.get('--port', '80')
    password = arguments.get('--password', None)
    if not password:
        password = getpass('Freebox password: ')
        
    client_mode = arguments.get('client', False)
    download_mode = arguments.get('download', False)
    
    
    fbx_client = freeboxClient(host, port, None, password)#params are host, port, username, password
    login_sucess = fbx_client.login()
    if client_mode:
        print "login success : %s" % login_sucess
    
    if download_mode:
        path_or_url = arguments.get('PATH_OR_URL', None)
        if not path_or_url:
            print u"Give a file torrent path or url"
        #no we will find if path_or_url is a path or an url
        torrent_file = None
        torrent_url = None
        
        if os.path.isfile(path_or_url):
            torrent_file = path_or_url
        else:
            torrent_url = path_or_url
        downloader = Downloader(fbx_client)
        downloader.add_file_to_download(torrent_file, torrent_url)
    
   
   
if __name__ == "__main__":
    try:
       main()
    except (KeyboardInterrupt, SystemExit):
        sys.exit()