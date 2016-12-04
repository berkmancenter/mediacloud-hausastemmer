#!/usr/bin/env python
# coding=utf-8

from setuptools import setup

setup(
    name='hausastemmer',
    version='1.0',
    description='Hausa language stemmer (Bimba et al., 2015)',
    long_description='''Hausa language stemmer reference implementation by Bimba et al., 2015. Uses Hausa affix-rules
and reference lookup to stem words in Hausa language.

Paper: Bimba, A., Idris, N., Khamis, N. and Noor, N.F.M. (2015) ‘Stemming Hausa text: Using affix-stripping rules and
reference look-up’, Language Resources and Evaluation, 50(3), pp. 687–703. doi: 10.1007/s10579-015-9311-x.
URL: https://bit.ly/hausa-stemming-bimba.

Based on modifications to the implementation of the Porter's Stemming Algorithm by Vivake Gupta (2001).

Copyright (C) 2013, Bimba Andrew Thomas <andrewbimba@gmail.com>, Department of Artificial Intelligence,
FSKTM Universiti Malaya, Kuala Lumpur, Malaysia.

Adapted as a Python module by Linas Valiukas <lvaliukas@cyber.law.harvard.edu>.
''',
    author='Andrew Bimba, Norisma Idris, Norazlina Khamis, Nurul Fazmidar Mohd Noor, Linas Valiukas',
    author_email='andrewbimba@gmail.com, lvaliukas@cyber.law.harvard.edu',
    url='https://github.com/pypt/mediacloud-hausastemmer',
    keywords="stemmer",
    license="BSD",
    packages=['hausastemmer'],
    package_dir={'hausastemmer': 'hausastemmer'},
    test_suite='nose.collector',
    tests_require=['nose'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python',
        'Natural Language :: Hausa',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Database',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Text Processing :: Indexing',
        'Topic :: Text Processing :: Linguistic'
    ]
)
