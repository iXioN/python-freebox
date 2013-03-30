# !/usr/bin/env python
# -*- coding: utf-8 -*-
#  freebox.py
#  python-freebox
#  
#  Created by antonin on 2013-03-29.
#  Copyright 2013 antonin. All rights reserved.
# 

#see
#http://www.chosesafaire.fr/2012/05/api-minimaliste-freebox-revolution/
#https://github.com/fdev31/pyFreebox/tree/master/freebox
#http://www.freebox-v6.fr/wiki/index.php?title=API#Transmission

#torrent link : http://cdimage.debian.org/debian-cd/6.0.7/amd64/bt-cd/debian-6.0.7-amd64-netinst.iso.torrent
#personal ip = "88.164.113.16:8000"


import sys
from getpass import getpass
from optparse import OptionParser

import json
import requests

class FreeboxException(Exception):
    pass
class WrongPassword(FreeboxException):
    pass

    
LOGIN_PAGE = "login.php"

DOWNLOAD_PAGE = "download.php"
DOWNLOAD_PAGE_API = "download.cgi"

class freeboxClient(object):
    """a simple freebox client api"""
    
    def __init__(self, freebox_ip=None, fbx_login=None, fbx_password=None):
        super(freeboxClient, self).__init__()
        self.freebox_ip = freebox_ip or 'mafreebox.free.fr'
        self.fbx_login = fbx_login or "freebox"
        self.fbx_password = fbx_password
        self.freebox_url = "http://%s" % self.freebox_ip
        
        self.session = requests.session()
    
    def login(self):
        """
        the login method
        """
        payload = {
            'login': self.fbx_login, 
            'passwd': self.fbx_password,
        }
        login_url = "%s/%s" % (self.freebox_url, LOGIN_PAGE)
        login_request = self.session.post(login_url, data=payload)
        self.session.auth = (self.fbx_login, self.fbx_password)
        
        if login_request.url == login_url: #TODO: another cheking method
             raise WrongPassword()
        return True
    
    def add_file_to_download(self, torrent_file, url_to_download):
        """ upload the torrent and start the download"""
        if torrent_file and url_to_download:
            raise('specify a file OR an url to download')
        
        files = None
        if torrent_file:
            files = {'file': open(torrent_file, 'rb')}  
        #action : download.cgi
        #encoded : multipart/form-data
        
        #csrf_token token :'(
        #input file : name data
        #method : value="download.torrent_add"
        download_url = "%s/%s" % (self.freebox_url, DOWNLOAD_PAGE_API) 
        download_page = "%s/%s" % (self.freebox_url, DOWNLOAD_PAGE)     
            
        payload = {
            'method':"download.torrent_add", 
            'csrf_token':"BakzNScFVqWLJnqKgB4lrpsRX1TYRNUVqpdTXgthcrusXQfwkFn+EO/0ap60U4AM",
            'user':"freebox",
            'ajax_iform':1,
            'url':url_to_download,
        }
        
        headers = {'Referer': download_page, "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:18.0) Gecko/20100101 Firefox/18.0", "Host":self.freebox_ip, "Content-Type":""}
        download_post_request = self.session.post(download_url, data=payload, headers=headers, files=files)
        print download_post_request
           
        


def main():
    parser = OptionParser(usage="usage: %prog filename",
                         version="%prog 0.1")
    parser.add_option("-i", "--freeboxip", dest="freebox_ip",
             help="the freebox ip addr", metavar="freebox_ip", default="")
    parser.add_option("-f", "--file", dest="torrent_file",
             help="the torrent file to download", metavar=".torrent", default="")
    parser.add_option("-u", "--url", dest="url_to_download",
               help="the http or magnet url", metavar="url", default="")
     
    (options, args) = parser.parse_args()

    password = getpass('Freebox password: ')
    
    freebox_ip = options.freebox_ip or 'mafreebox.free.fr'
    fbx_client = freeboxClient(freebox_ip=freebox_ip, fbx_password=password)
    fbx_client.login()
    
    torrent_file = options.torrent_file
    url_to_download = options.url_to_download
    fbx_client.add_file_to_download(torrent_file, url_to_download)
    
   
   
if __name__ == "__main__":
    try:
       main()
    except (KeyboardInterrupt, SystemExit):
        sys.exit()