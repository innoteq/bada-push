#!/usr/bin/env python
import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__author__ = 'Alexey Goditskiy <godickii@gmail.com>'
__version__ = '0.4'

setup(
    name='python-bada-push',
    version=__version__,

    # Package dependencies.
    install_requires=['requests==1.1.0', 'simplejson==3.1.0'],

    # Metadata for PyPI.
    author='Alexey Goditskiy',
    author_email='godickii@gmail.com',
    license='BSD',
    url='https://bitbucket.org/godickii/python-samsung-bada-push-client',
    keywords='python samsung bada push messaging',
    description='Python module for push messaging service for Samsung Bada.',
    long_description=open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'README.md')), 'rb').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Communications :: Telephony',
        'Topic :: Internet'
    ],
    packages=['bada_push'],
    platforms='any',
)
