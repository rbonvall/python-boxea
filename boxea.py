#!/usr/bin/env python
# encoding: utf-8

from __future__ import unicode_literals
import re
import sys
import copy

# for Py2 and Py3 compatibility
try:
    unicode
except NameError:
    def unicode(x, *args, **kwargs):
        return str(x)


symbols = dict(
   ns='│',   we='─',            NS='║',   WE='═',
   se='┌',  swe='┬',  sw='┐',   SE='╔',  SWE='╦',  SW='╗',
  nse='├', nswe='┼', nsw='┤',  NSE='╠', NSWE='╬', NSW='╣',
   ne='└',  nwe='┴',  nw='┘',   NE='╚',  NWE='╩',  NW='╝',
   sE='╒',  sWE='╤',  sW='╕',   Se='╓',  Swe='╥',  Sw='╖',
  nsE='╞', nsWE='╪', nsW='╡',  NSe='╟', NSwe='╫', NSw='╢',
   nE='╘',  nWE='╧',  nW='╛',   Ne='╙',  Nwe='╨',  Nw='╜',
)


def neighbors(s):
    return list(s), list(s), list(s), list(s)

def ascii_to_box(text):
    return text

def main():
    print(ascii_to_box(unicode(sys.stdin.read(), encoding='utf-8')))

if __name__ == '__main__':
    main()

