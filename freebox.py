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

import sys
from optparse import OptionParser

import json
import requests

class FreeboxException(Exception):
    pass
class WrongPassword(FreeboxException):
    pass

class freeboxClient(object):
    """a simple freebox client api"""
    
    def __init__(self, freebox_ip=None, fbx_login=None, fbx_password=None):
        super(freeboxClient, self).__init__()
        self.freebox_ip = freebox_ip or "88.164.113.16:8000"
        self.fbx_login = fbx_login or "freebox"
        self.fbx_password = fbx_password
    
    def login(self):
        """
        the login method
        """
        payload = {
            'login': self.fbx_login, 
            'fbx_password': self.fbx_password,
        }
        login_url = "http://%s/login.php" % (self.freebox_ip)
        login_request = requests.post(login_url, data=payload)
        if not login_request.ok : #TODO: renforce the status check if needed, the freebox seems return a 200 even if a bad password
             raise WrongPassword()
        return True
        

if __name__ == "__main__":
    try:
        parser = OptionParser(usage="usage: %prog filename",
                              version="%prog 0.1")
        parser.add_option("-p", "--password", dest="password",
                  help="your freebox password", metavar="your_password", default="")
        (options, args) = parser.parse_args()
        
        #TODO : exit if no password or set the arg as requiered
        password = options.password
        fbx_client = freeboxClient(fbx_password=password)
        fbx_client.login()
        
        
    except (KeyboardInterrupt, SystemExit):
        sys.exit()