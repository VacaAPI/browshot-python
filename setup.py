import os
import sys

from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

requirements = ['urllib2', 'simplejson', 'urllib']

setup(
	name='Browshot',
	version='1.2.0',
	py_modules=['browshot'],
	description='Client to intereact with Browshot',
    long_description=read('README'),
    url='http://www.browshot.com/api/documentation',
    license='Apache',
    author='Julien Sobrier',
    author_email='julien@sobrier.net',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
	packages=find_packages(),
    namespace_packages=["browshot"],
    install_requires=requirements,
)