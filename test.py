#!/usr/bin/env python
# encoding: utf-8

from __future__ import unicode_literals
import unittest
import boxea

# for Py2 and Py3 compatibility
try:
    unicode
except NameError:
    def unicode(x, *args, **kwargs):
        return str(x)


def parse_cases(filename):
    content = unicode(open(filename).read().strip(), encoding='utf-8')
    test_cases = [ tuple(test.split(2 * '\n'))
                   for test in content.split(3 * '\n') ]
    return test_cases


class TestAsciiToBox(unittest.TestCase):

    def setUp(self):
        self.test_cases = parse_cases('test_cases.txt')

    def test_ascii_to_box(self):
        for i, o in self.test_cases:
            result = boxea.ascii_to_box(i)
            self.assertEqual(result, o)


class TestNeighbors(unittest.TestCase):

    def setUp(self):
        self.input_string = (
            'abc\n'
            'defg\n'
            '\n'
            'hijklm\n'
            'nopq\n'
        )
        self.n, self.s, self.w, self.e = boxea.neighbors(self.input_string)

    def test_neighbors_lengths(self):
        self.assertEqual(len(self.n), len(self.input_string))
        self.assertEqual(len(self.s), len(self.input_string))
        self.assertEqual(len(self.w), len(self.input_string))
        self.assertEqual(len(self.e), len(self.input_string))

    def test_north(self):
        self.assertEqual(self.n, [
            None, None, None, None,
            'a', 'b', 'c', '\n', None,
            'd',
            '\n', None, None, None, None, None, None,
            'h', 'i', 'j', 'k', 'l',
        ])

    def test_south(self):
        self.assertEqual(self.s, [
            'd', 'e', 'f', 'g',
            '\n', None, None, None, None,
            'h',
            'n', 'o', 'p', 'q', '\n', None, None,
            None, None, None, None, None,
        ])

    def test_west(self):
        self.assertEqual(self.w, [
            None, 'a', 'b', 'c',
            None, 'd', 'e', 'f', 'g',
            None,
            None, 'h', 'i', 'j', 'k', 'l', 'm',
            None, 'n', 'o', 'p', 'q',
        ])

    def test_east(self):
        self.assertEqual(self.e, [
            'b', 'c', '\n', None,
            'e', 'f', 'g', '\n', None,
            None,
            'i', 'j', 'k', 'l', 'm', '\n', None,
            'o', 'p', 'q', '\n', None,
        ])


if __name__ == '__main__':
    unittest.main()

