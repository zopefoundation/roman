from setuptools import setup


desc = ('%s/n/n%s' % (open('README.rst').read(), open('CHANGES.txt').read()))

setup(
    name='roman',
    version='3.3',
    author="Mark Pilgrim",
    author_email="f8dy@diveintopython.org",
    description="Integer to Roman numerals converter",
    long_description=desc,
    license="Python 2.1.1",
    keywords="roman",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'License :: OSI Approved :: Python Software Foundation License',
        'Programming Language :: Python',
        'Natural Language :: English',
        'Operating System :: OS Independent'],
    url='https://github.com/zopefoundation/roman',
    package_dir={"": "src"},
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*',
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
