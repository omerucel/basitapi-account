# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages
import basitapi_account

def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

setup(
    name='basitapi-account',
    version=basitapi_account.__version__,
    description=read('DESCRIPTION'),
    long_description=read('README.md'),
    licence='The MIT LICENCE',
    platforms=['OS Independent'],
    keywords='basitapi, django, api, account, access-token',
    author='Ömer ÜCEL',
    author_email='omerucel@gmail.com',
    url='https://github.com/omerucel/basitapi-account',
    packages=find_packages(exclude=['tests', 'cover']),
    include_package_data=True,
    install_required=[
        'Django',
    ]
)
