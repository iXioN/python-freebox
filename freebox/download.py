# !/usr/bin/env python
# -*- coding: utf-8 -*-
#  download.py
#  python-freebox
#  
#  Created by antonin on 2013-04-05.
#  Copyright 2013 antonin. All rights reserved.
# 

DOWNLOAD_PAGE = "download.php"
DOWNLOAD_PAGE_API = "download.cgi"


ERROR_CODE_MAPPING = {
        11:'error occured'
}    

 
class Downloader(object):
    """get a client """
    def __init__(self, client):
        super(Downloader, self).__init__()
        #TODO : check the need login
        self.client = client
        
    def add_file_to_download(self, torrent_file, url_to_download):
        """ upload the torrent and start the download"""
        if torrent_file and url_to_download:
            raise('specify a file OR an url to download')
        
        download_page = "%s/%s" % (self.client.freebox_url, DOWNLOAD_PAGE)
        #get the page to get csrf token
        csrf_token = self.client.get_csrf_token(download_page)
        
        files = None
        if torrent_file:
            files = {'data': open(torrent_file, 'rb')}  
            
        download_url = "%s/%s" % (self.client.freebox_url, DOWNLOAD_PAGE_API) 
        payload = {
            'method':"download.torrent_add", 
            'csrf_token':csrf_token,
            'user':"freebox",
            'ajax_iform':1,
            'url':"" if url_to_download is None else url_to_download,
        }
        if not torrent_file:
            payload['data'] = None
        download_post_request, result = self.client.post(download_url, payload, files=files)
        if result:
            if 'errcode' in result:
                print "Error while adding download : %s" % ERROR_CODE_MAPPING[result['errcode']]
                return
            else:
                print "Downdload OK, id : %s" % (result.get('result', None))
                return
        print "Error while adding download http status: %s " % (download_post_request)