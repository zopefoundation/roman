##############################################################################
#
# Copyright (c) 2001 Mark Pilgrim and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################

from setuptools import setup


desc = ('{}\n\n{}'.format(open('README.rst').read(),
                          open('CHANGES.rst').read()))

setup(
    name='roman',
    version='4.1.dev0',
    author="Mark Pilgrim",
    maintainer="Zope Foundation and Contributors",
    maintainer_email="zope-dev@zope.dev",
    description="Integer to Roman numerals converter",
    long_description=desc,
    long_description_content_type='text/x-rst',
    license="ZPL-2.1",
    keywords="roman",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'License :: OSI Approved :: Python Software Foundation License',
        'Programming Language :: Python',
        'Natural Language :: English',
        'Operating System :: OS Independent',
    ],
    url='https://github.com/zopefoundation/roman',
    package_dir={"": "src"},
    python_requires='>=3.7',
    py_modules=["roman"],
    include_package_data=True,
    test_suite='tests',
    zip_safe=True,
    entry_points={
        'console_scripts': [
            'roman=roman:main',
        ]
    }
)
