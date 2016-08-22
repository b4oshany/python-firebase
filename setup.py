#!/usr/bin/env python
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    long_description = readme.read()


setup(name='python-firebase-gae',
      version='1.0.0',
      description="Python interface to the Firebase's REST API.",
      long_description=long_description,
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.2',
          'Natural Language :: English',
      ],
      keywords='firebase python gae google appengine',
      author='Ozgur Vatansever',
      author_email='ozgurvt@gmail.com',
      maintainer='Oshane Bailey',
      maintainer_email='b4.oshany@gmail.com',
      url='http://ozgur.github.com/python-firebase/',
      license='MIT',
      packages=['firebase'],
      test_suite='tests.all_tests',
      install_requires=['requests==2.3.0', 'webob==1.6.1'],
      zip_safe=False,
)
