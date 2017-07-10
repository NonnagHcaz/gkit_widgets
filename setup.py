#! /usr/bin/env python

from __future__ import absolute_import, print_function, division
try:
    from setuptools import setup, find_packages
except ImportError:
    raise RuntimeError('No suitable version of setuptools detected.')
import re
import os
import codecs

HERE = os.path.abspath(os.path.dirname(__file__))

###############################################################################


def read(*parts):
    with codecs.open(os.path.join(HERE, *parts), 'rb', 'utf-8') as f:
        return f.read()


META_FILE = read(* ['docs', '__about__.py'])


def find_meta(meta):
    meta_match = re.search(
        r"^__{meta}__ = ['\"]([^'\"]*)['\"]".format(meta=meta),
        META_FILE,
        re.M)

    if meta_match:
        return meta_match.group(1)
    raise RuntimeError("Unable to find __{meta}__ string.".format(meta=meta))


setup(
    name=find_meta('title'),
    version=find_meta('version'),
    url=find_meta('uri'),
    license=find_meta('license'),
    author=find_meta('author'),
    author_email=find_meta('email'),
    description=find_meta('summary'),
    maintainer=find_meta('author'),
    maintainer_email=find_meta('email'),
    keywords=[],
    long_description=read(* ['docs', 'README.rst']),
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    zip_safe=False,
    classifiers=find_meta('classifiers').split('\n'),
    include_package_data=True,
    test_suite='tests')
