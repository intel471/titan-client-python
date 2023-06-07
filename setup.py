# coding: utf-8

"""
    Titan API v1

    Official low-level client for Intel 471's Titan API. It aims at providing common ground for all the endpoints in Python.

    The version of the OpenAPI document: 1.19.7
    Generated by: https://openapi-generator.tech
"""

from pkg_resources import parse_requirements
from setuptools import setup, find_packages  # noqa: H301

NAME = "Titan Client"
VERSION = "1.19.7"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

with open("requirements.txt", "r") as requirements_txt:
    reqs = parse_requirements(requirements_txt)
    REQUIRES = [str(req) for req in reqs]

setup(
    name=NAME,
    version=VERSION,
    description="Titan API v1",
    author="Intel 471 Inc.",
    author_email="support@intel471.com",
    license="MIT",
    url="https://github.com/intel471/titan-client-python",
    keywords=["OpenAPI", "OpenAPI-Generator", "Titan API v1"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\
    Official low-level client for Intel 471's Titan API. It aims at providing common ground for all the endpoints in Python.
    """
)
