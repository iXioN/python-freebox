#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  setup.py
#  python-freebox
#  
#  Created by Antonin Lacombe on 2013-04-04.
#  Copyright 2013 Antonin Lacombe. All rights reserved.
# 

import sys
from setuptools import setup

requirements = open('requirements.txt').readlines()

setup(name='freebox',
    version='0.1-dev',
    license='LGPLv3',
    description='a freebox (French set-top box) python client and cli  management',
    long_description=open('README.md').read(),
    classifiers=['Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: English'],
    keywords='freebox',
    author='Antonin Lacombe',
    author_email='antonin.lacombe@gmail.com',
    url='https://github.com/iXioN/python-freebox.git',
    packages=['freebox', ],
    entry_points={
        'console_scripts': ['freebox = freebox.freebox:main'],#TODO : add downloader
    },
    #test_suite='python-freebox.tests.suite',
    install_requires=requirements,)
