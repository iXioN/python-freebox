# !/usr/bin/env python
# -*- coding: utf-8 -*-
#  client.py
#  python-freebox
#  
#  Created by antonin on 2013-04-05.
#  Copyright 2013 antonin. All rights reserved.
# 


import json
import requests
from bs4 import BeautifulSoup

class FreeboxException(Exception):
    pass
class WrongPassword(FreeboxException):
    pass

    
LOGIN_PAGE = "login.php"

class freeboxClient(object):
    """a simple freebox client api"""
    
    def __init__(self, host='mafreebox.free.fr', port='80', username='freebox', password=''):
        super(freeboxClient, self).__init__()
        self.host = host
        self.port = port
        self.username = username or "freebox"
        self.password = password
        self.freebox_url = "http://%s:%s" % (self.host, self.port)
        
        self.session = requests.session()
    
    #simple method 
    def login(self):
        """
        the login method
        """
        payload = {
            'login': self.username, 
            'passwd': self.password,
        }
        login_url = "%s/%s" % (self.freebox_url, LOGIN_PAGE)
        login_request = self.session.post(login_url, data=payload)
                
        if login_request.url == login_url: #TODO: another cheking method
             raise WrongPassword()
        return True
    
    def post(self, url, payload, files):
        """simple post, if resutl is a textarea with key value form, return a dict with the values"""
        post_request = self.session.post(url, data=payload, files=files)
        if post_request.ok:
            result = None
            soup = BeautifulSoup(post_request.content)
            try:
                result = json.loads(soup.text)
            except (AttributeError, AttributeError), e:
                pass
            return post_request, result
        return post_request, None
    
    def get(self, url):
        """simple get"""
        return self.session.get(url)
    
    #method to acces and post some datas
    def get_csrf_token(self, url):
        """get the crsf token in the page url"""
        request_page = self.get(url)
        soup = BeautifulSoup(request_page.content)
        csrf_input = soup.find('input', {'name': 'csrf_token'})
        return csrf_input.attrs.get('value', None)
    