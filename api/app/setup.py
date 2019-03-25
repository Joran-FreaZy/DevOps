#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages
import pkg_resources

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    

def _parse_requirements(filepath):
    pip_version = list(map(int, pkg_resources.get_distribution('pip').version.split('.')[:2]))
    if pip_version >= [10, 0]:
        from pip._internal.download import PipSession
        from pip._internal.req import parse_requirements
        raw = parse_requirements(filepath, session=PipSession())
    elif pip_version >= [6, 0]:
        from pip.download import PipSession
        from pip.req import parse_requirements
        raw = parse_requirements(filepath, session=PipSession())
    else:
        from pip.req import parse_requirements
        raw = parse_requirements(filepath)

    return [str(i.req) for i in raw]

#requirements = [str(i.req) for i in parse_requirements("requirements.txt", session=False)]
#test_requirements = [str(i.req) for i in parse_requirements("test_requirements.txt", session=False)]

requirements=_parse_requirements("requirements.txt")
test_requirements=_parse_requirements("test_requirements.txt")
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




