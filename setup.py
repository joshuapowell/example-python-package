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
    packages=["endor"],
    include_package_data=True,
    install_requires=[
        "flask",
    ],
)
