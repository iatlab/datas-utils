# -*- coding:utf-8 -*-
from setuptools import setup

setup(
    name = "datas_utils",
    packages = ["datas_utils", 
                "datas_utils.env",
                "datas_utils.log",
                "datas_utils.aws",
               ],
    version = "0.0.1",
    description = "Tools for Datas Project",
    author = "Makoto P. Kato",
    author_email = "mpkato@acm.org",
    license     = "MIT License",
    url = "https://github.com/iatlab/datas_utils",
    install_requires = ['boto3>=1.9.3', 'mysql-connector-python>=8.0.12'],
    tests_require=['nose'],
)
