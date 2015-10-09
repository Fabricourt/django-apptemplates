#!/usr/bin/env python
from os.path import dirname, join
from setuptools import setup, find_packages

version = '0.3'


def read(fname):
    return open(join(dirname(__file__), fname)).read()

setup(name='django-apptemplates',
      version=version,
      description='Django template loader that allows you to load and'
                  'override a template from a specific Django application.',
      long_description=read('README.rst'),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.4',
          'Programming Language :: Python :: 2.5',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
          'Topic :: Internet :: WWW/HTTP :: WSGI',
          'Topic :: Software Development :: Libraries :: Application Frameworks',  # noqa
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='django,template,loader',
      author='Konrad Wojas',
      author_email='bitbucket@m.wojas.nl',
      maintainer='Peter Bittner',
      maintainer_email='django@bittner.it',
      url='http://bitbucket.org/bittner/django-apptemplates/',
      license='MIT License',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
)
