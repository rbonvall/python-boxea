Boxea
=====
Convert ASCII-art box drawings to prettier versions
by using `box-drawing Unicode symbols`_ (ANSI-art).

.. _box-drawing Unicode symbols: http://en.wikipedia.org/wiki/Box-drawing_characters

Usage
-----
The script uses standard input and output::

    $ cat example
    +-----+-----+
    | abc | def |
    +-----+-----+
    |  12 |   0 |
    |   4 |  72 |
    +-----+-----+

    $ boxea.py < example
    ┌─────┬─────┐
    │ abc │ def │
    ├─────┼─────┤
    │  12 │   0 │
    │   4 │  72 │
    └─────┴─────┘

It can also be used as a Python module::

    >>> import boxea
    >>> s = u'''
    ... +---+
    ... | a |
    ... +---+'''
    >>> print boxea.ascii_to_box(s)

    ┌───┐
    │ a │
    └───┘

To-do
-----
* Support double lines (``═══``).
* Support thicker lines (``━━━``).
* Allow to use characters other than ``+``, ``-`` and ``|``.
* Better command-line interface (options, file name arguments).
* Create ``setup.py`` script.
* Upload to PyPI.
* Choose a license.

Patches are welcome.

Author
------
Roberto Bonvallet <rbonvall@gmail.com>

