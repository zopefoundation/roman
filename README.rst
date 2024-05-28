.. image:: https://github.com/zopefoundation/roman/actions/workflows/tests.yml/badge.svg
    :target: https://github.com/zopefoundation/roman/actions/workflows/tests.yml

.. image:: https://coveralls.io/repos/github/zopefoundation/roman/badge.svg?branch=master
    :target: https://coveralls.io/github/zopefoundation/roman?branch=master

.. image:: https://img.shields.io/pypi/v/roman.svg
    :target: https://pypi.org/project/roman/
    :alt: Current version on PyPI

.. image:: https://img.shields.io/pypi/pyversions/roman.svg
    :target: https://pypi.org/project/roman/
    :alt: Supported Python versions

roman
=====

Small helper library to convert arabic to roman numerals.

There are two ways to use this library.

1. Importing it into your application

.. code-block:: python

    import roman

    # to roman
    number = int(input('> ')) # 10
    print(roman.toRoman(number))

    # from roman
    number = input('> ') # X
    print(roman.fromRoman(number))


2. ``roman`` CLI command

.. code-block:: bash

    ~$ roman 972
    CMLXXII
    # use the -r/--reverse to convert Roman numerals
    ~$ roman -r CMLXXII
    972
    # case insensitive
    ~$ roman -r cMlxxii
    972

