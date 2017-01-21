#!/usr/bin/env python

"""Endor Example Package Installer.

A demonstration of how to create a Python application that can be installed
via `pip.
"""

from setuptools import setup

setup(
    name="endor",
    version="0.0.1-dev",
    description="An example Python Package",
    url="https://github.com/joshuapowell/example-python-package",
    author="Joshua Powell",
    license="MIT",
    keywords="python setuptools example package installer pip",
    packages=["endor"],
    include_package_data=True,
    install_requires=[
        "flask",
    ],
)
