#!/usr/bin/env python
import os
import subprocess
import sys

root = os.path.dirname(__file__)

def bootstrap_other():
    if not os.path.exists(os.path.join(root, 'bin', 'python')):
        subprocess.check_call("virtualenv %s" % root, shell=True)

def bootstrap_darwin():
    """
    darwin specific bootstrap. We need virtualenv from the ports because boost is
    linkeds agains ports' python , and they do not seem to be binary compatible
    """    
    if not os.path.exists(os.path.join(root, 'bin', 'python')):
        subprocess.check_call("/opt/local/bin/virtualenv-2.7 %s" % root, shell=True)
    

def main():
    
    bootstrap = bootstrap_other

    if sys.platform == 'darwin':
        bootstrap = bootstrap_darwin
        
    bootstrap()



if __name__ == '__main__':
    main()