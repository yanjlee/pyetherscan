from distutils.core import setup
from setuptools import find_packages
from os import path
import sys

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
if sys.version_info[0] < 3:
    with open(path.join(here, 'README.rst'), 'rb') as f:
        long_description = f.read()
else:
    with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()

setup(
    name='pyetherscan_pro',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    version='1.1.2',
    description='An unofficial wrapper for the Etherscan.io API',
    long_description=long_description,
    author='yanjlee',
    author_email='yanjlee@163.com',
    url='https://github.com/yanjlee/pyetherscan',
    download_url='https://github.com/Marto32/pyetherscan/archive/0.1.2.tar.gz',
    keywords=['ethereum', 'blockchain', 'etherscan'],
    license='MIT License',
    install_requires=[
        'requests',
        'faker',
        'execjs',
        'loguru',
        'base64',
        'hashlib',
        'Crypto',
        'pandas',
        'fuzzywuzzy',
        'httpx',
        'Pillow',
        'playwright',
        'PyExecJS',
        'redis',
        'fastapi',
        'uvicorn',
        'APScheduler',
        'beautifulsoup4',
        'bs4',
        'certifi',
        'clickhouse-driver',
        'curl-cffi',
        'DrissionPage',
        'fake-useragent',
        'Flask',
        'Flask-APScheduler',
        'Flask-Cors',
        'frida',
        'gevent',
        'httpx',
        'Jinja2',
        'langchain',
        'langchain-community',
        'suiutils-py',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
