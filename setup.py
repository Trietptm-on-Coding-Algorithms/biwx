#!/usr/bin/env python2.7
# coding: UTF-8


from setuptools import setup
import os
import shutil
import biwx

if not os.path.exists('scripts'):
    os.makedirs('scripts')
shutil.copyfile('biwx.py', 'scripts/biwx')

with open('README.rst', 'r') as f:
    readme_file = f.read()

setup(
    name='biwx',
    version=biwx.__version__,
    author=biwx.__author__,
    author_email='i.am.tkmru@gmail.com',
    scripts=['scripts/biwx'],
    url='https://github.com/tkmru/biwx',
    license=biwx.__license__,
    keywords=['binary', 'hex'],
    description=biwx.__description__,
    long_description=readme_file,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License'
    ]
)
