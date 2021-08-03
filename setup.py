import os
import re

from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), "sqlalchemy_tidb", "__init__.py")) as v:
    version = re.compile(r'.*__version__ = "(.*?)"', re.S).match(v.read()).group(1)

readme = os.path.join(os.path.dirname(__file__), "README.md")

dependencies = ["sqlalchemy>=1.4"]

setup(
    name="sqlalchemy-tidb",
    version=version,
    author="Weizhen Wang",
    author_email="wangweizhen@pingcap.com",
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
            "tidb = sqlalchemy_tidb.mysqlconnector:TiDBDialect_mysqlconnector",
            "tidb.pyodbc = sqlalchemy_tidb.pyodbc:TiDBDialect_pyodbc",
            "tidb.mysqlconnector = sqlalchemy_tidb.mysqlconnector:TiDBDialect_mysqlconnector",
        ]
    },
)