from setuptools import setup

setup (
    name='roman',
    version='1.4.0',
    author = "Mark Pilgrim",
    author_email = "f8dy@diveintopython.org",
    description = "Integer to Roman numerals converter",
    license = "Python 2.1.1",
    keywords = "roman",
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Python Software Foundation License',
        'Programming Language :: Python',
        'Natural Language :: English',
        'Operating System :: OS Independent'],
    url = 'http://pypi.python.org/pypi/roman',
    package_dir={"": "src"},
    py_modules=["roman"],
    include_package_data = True,
    zip_safe = True,
    )
