#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages
from pip.req import parse_requirements


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

requirements = [str(i.req) for i in parse_requirements("requirements.txt", session=False)]
test_requirements = [str(i.req) for i in parse_requirements("test_requirements.txt", session=False)]

VERSION = '0.1.0'

setup(
    name='myapi',
    version=str(VERSION),
    long_description="",
    author='Damien Goldenberg',
    author_email='damdam.gold@gmail.com',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='api',
    classifiers=[],
    test_suite='tests',
    tests_require=test_requirements,
    scripts=['bin/api-run', 'bin/swagger.yaml'],
)
