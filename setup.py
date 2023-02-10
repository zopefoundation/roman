from setuptools import setup


desc = ('{}\n\n{}'.format(open('README.rst').read(),
                          open('CHANGES.txt').read()))

setup(
    name='roman',
    version='4.0.dev0',
    author="Mark Pilgrim",
    author_email="zope-dev@zope.dev",
    description="Integer to Roman numerals converter",
    long_description=desc,
    long_description_content_type='text/x-rst',
    license="Python 2.1.1",
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
