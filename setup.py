from __future__ import print_function

from setuptools import setup
import sys

import unittest

def test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('foalorm.orm.tests', pattern='test_*.py')
    return test_suite

name = "foalorm"
version = __import__('foalorm').__version__
description = "Foal Object-Relational Mapper"
long_description = """
About
=========
FoalORM is an advanced object-relational mapper forked from PonyORM.

Installation
=================
::

    pip install foalorm

"""

classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: Implementation :: PyPy',
    'Topic :: Software Development :: Libraries',
    'Topic :: Database'
]

author_email = "me@frodo821.me"
author = f'frodo821 <{author_email}>'
project_urls = {
    "Source": "https://github.com/frodo821/foalorm",
}
license = "MIT License"

packages = [
    "foalorm",
    "foalorm.flask",
    "foalorm.flask.example",
    "foalorm.orm",
    "foalorm.orm.dbproviders",
    "foalorm.orm.examples",
    "foalorm.orm.integration",
    "foalorm.orm.tests",
    "foalorm.thirdparty",
    "foalorm.utils"
]

package_data = {
    'foalorm.flask.example': ['templates/*.html'],
    'foalorm.orm.tests': ['queries.txt']
}

download_url = "http://pypi.python.org/pypi/pony/"

if __name__ == "__main__":
    pv = sys.version_info[:2]
    if pv not in ((3, 6), (3, 7), (3, 8), (3, 9), (3, 10)):
        s = "Sorry, but %s %s requires Python of one of the following versions: 3.6-3.10." \
            " You have version %s"
        print(s % (name, version, sys.version.split(' ', 1)[0]))
        sys.exit(1)

    setup(
        name=name,
        version=version,
        description=description,
        long_description=long_description,
        classifiers=classifiers,
        author=author,
        author_email=author_email,
        project_urls=project_urls,
        license=license,
        packages=packages,
        package_data=package_data,
        download_url=download_url,
        test_suite='setup.test_suite'
    )
