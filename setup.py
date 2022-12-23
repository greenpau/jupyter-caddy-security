# coding: utf-8

from setuptools import find_packages
from setuptools import setup

__version__ = '1.0.0'

with open("README.md") as fh:
    long_description = fh.read()

setup(
    name="jupyter-caddy-security",
    version=__version__,
    description="Jupyter Identity Provider and Authorizer for Caddy Security",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/greenpau/jupyter-caddy-security",
    author="Paul Greenberg",
    author_email="greenpau@outlook.com",
    license='License :: OSI Approved :: Apache Software License',
    packages=find_packages(),
    install_requires=["jupyterlab", "requests"],
    include_package_data=True,
    keywords=["Identity Provider", "Authorizer", "Jupyter"],
)
