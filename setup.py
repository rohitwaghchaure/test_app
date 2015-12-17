# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='test_app',
    version=version,
    description='To test differnt integrations with erpnext',
    author='Indictrans',
    author_email='rohit.w@indictranstech.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
