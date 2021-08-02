import os
import re

from setuptools import setup, find_packages

BASE_DIR = os.path.dirname(__file__)
VERSION_FILENAME = os.path.join(BASE_DIR, "version.py")
PACKAGE_INFO = {}
with open(VERSION_FILENAME) as f:
    exec(f.read(), PACKAGE_INFO)
version = PACKAGE_INFO["__version__"]

readme = os.path.join(os.path.dirname(__file__), "README.md")

dependencies = ["sqlalchemy>=1.4"]

setup(
    name="sqlalchemy-tidb",
    version=version,
    author="Cockroach Labs",
    author_email="cockroach-db@googlegroups.com",
    url="https://github.com/hawkingrei/sqlalchemy-tidb",
    description="tidb dialect for SQLAlchemy",
    long_description=open(readme).read(),
    long_description_content_type="text/markdown",
    license="http://www.apache.org/licenses/LICENSE-2.0",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    keywords="SQLAlchemy TiDB",
    install_requires=dependencies,
    packages=find_packages(include=["sqlalchemy_tidb"]),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        "sqlalchemy.dialects": [
            "tidb = sqlalchemy_tidb:TiDBDialect"
        ]
    },
)