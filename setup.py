#!/usr/bin/env python3
# sourcemanagement
# Copyright(C) 2020 Sai Sankar Gochhayat
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Setup file for source-management."""

import os
import setuptools
from pathlib import Path


def get_install_requires():
    """Fetch requirements from requirements file."""
    with open("requirements.txt", "r") as requirements_file:
        # TODO: respect hashes in requirements.txt file
        res = requirements_file.readlines()
        return [req.split(" ", maxsplit=1)[0] for req in res if req]


def get_version():
    """Fetch requirements from init file."""
    with open(os.path.join("thoth/sourcemanagement", "__init__.py")) as f:
        content = f.readlines()

    for line in content:
        if line.startswith("__version__ ="):
            # dirty, remove trailing and leading chars
            return line.split(" = ")[1][1:-2]
    raise ValueError("No version identifier found")


VERSION = get_version()

setuptools.setup(
    name="thoth-sourcemanagement",
    version=VERSION,
    author="Sai Sankar Gochhayat",
    author_email="saisankargochhayat@gmail.com",
    description="This package helps thoth app's interact with git forges like Github, Gitlab.",
    long_description=Path("README.rst").read_text(),
    url="https://github.com/thoth-station/source-management",
    license="GPLv3+",
    packages=["thoth.sourcemanagement"],
    install_requires=get_install_requires(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
