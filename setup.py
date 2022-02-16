#!/usr/bin/env python
"""This file contains setup instructions for pytd package."""
import codecs
import os

from setuptools import setup
import setuptools

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

with open(os.path.join(here, "pytd", "version.py")) as fp:
    exec(fp.read())

setup(
    name="pytd-youtube-downloader",
    version=__version__,
    author="Ikhwan S. H",
    author_email="ikhwansyatricha@gmail.com",
    package_data={"": ["LICENSE"],},
    url="https://github.com/perfect-less/Python-YouTube-Downloader",
    license="The Unlicense (Unlicense)",
    entry_points={
        "console_scripts": [
            "pytd = pytd.cli:main"],},
    classifiers=[
        "Development Status :: Beta/Unstable",
        "Environment :: Console",
        "License :: OSI Approved :: The Unlicense (Unlicense)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python",
        "Topic :: Video",
        "Topic :: Terminals",
    ],
    packages=[
        'pytd',
        'pytd.src',
        'pytd.settings',
        'pytd.pytdutils',
        'pytd.pytdutils.postprocess',
        'pytd.pytdutils.pytdout',
    ],
    install_requires=[
        'pytube',
    ],
    description=("Python application for downloading YouTube Videos."),
    long_description_content_type="text/markdown",
    long_description=long_description,
    python_requires=">=3.6",
)
