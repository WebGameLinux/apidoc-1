#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if sys.version_info < (3, 2):
    print("ApiDoc requires Python 3.2 or later")
    raise SystemExit(1)

if (3, 2) <= sys.version_info < (3, 3):
    requirements = ['Jinja2 == 2.6', 'PyYAML', 'jsonschema']
else:
    requirements = ['Jinja2', 'PyYAML', 'jsonschema']

from setuptools import setup, find_packages

setup(
    name='ApiDoc',
    version='1.0',
    description='Api Documentation Generator',
    author='Jérémy Derussé',
    author_email='jeremy@derusse.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
    ],
    platforms=['Any'],
    packages=find_packages(exclude=['tests', 'tests.*']),
    entry_points={
        'console_scripts': [
            'apidoc-analyse = apidoc.command.analyse:main',
            'apidoc-render = apidoc.command.render:main',
            'apidoc-watch = apidoc.command.watch:main',
        ],
    },
    include_package_data=True,
    package_data={'apidoc': [
        'template/*.html',
        'template/helper/*.html',
        'template/partial/*.html',
        'template/resource/css/*.css',
        'template/resource/js/*.js',
        'template/resource/img/*.png',
        'template/resource/font/*',
        'datas/schemas/*.yml',
        'command/logging.yml',
    ]},
    install_requires=requirements
)
