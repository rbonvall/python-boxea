#!/usr/bin/env python3
# encoding: utf-8

from __future__ import unicode_literals
import sys
from itertools import chain, islice
from operator import itemgetter

# for Py2 and Py3 compatibility
try:
    unicode
except NameError:
    def unicode(x, *args, **kwargs):
        return str(x)
try:
    from itertools import izip_longest as zipl
except ImportError:
    from itertools import zip_longest as zipl


symbols = dict(
   se='┌',  swe='┬',  sw='┐',   SE='╔',  SWE='╦',  SW='╗',
  nse='├', nswe='┼', nsw='┤',  NSE='╠', NSWE='╬', NSW='╣',
   ne='└',  nwe='┴',  nw='┘',   NE='╚',  NWE='╩',  NW='╝',
   sE='╒',  sWE='╤',  sW='╕',   Se='╓',  Swe='╥',  Sw='╖',
  nsE='╞', nsWE='╪', nsW='╡',  NSe='╟', NSwe='╫', NSw='╢',
   nE='╘',  nWE='╧',  nW='╛',   Ne='╙',  Nwe='╨',  Nw='╜',
   ns='│',   we='─',            NS='║',   WE='═',
    n='╵',    s='╷',
    w='╴',    e='╶',
)

def flatten(lists):
    return list(chain(*lists))


def neighbors(text):
    '''Return iterables n, s, w and e of neighbors of text.

    For a given text, return four character-yielding iterables that are
    respectively the neighbors above, below, to the left and to the right of
    the corresponding character in the text.  Inexistant neighbors are
    represented by None.
    '''

    lines = text.splitlines(True)

    n = [None for _ in lines[0]] + flatten([
        map(itemgetter(0), islice(zipl(prev_line, line), len(line)))
        for prev_line, line in zip(lines, lines[1:])
    ])
    s = flatten([
        map(itemgetter(1), islice(zipl(line, next_line), len(line)))
        for line, next_line in zip(lines, lines[1:])
    ]) + [None for _ in lines[-1]]

    w = flatten([[None] + list(line[:-1]) for line in lines])
    e = flatten([list(line[1:]) + [None]  for line in lines])

    return n, s, w, e


def ascii_to_box(text, vertical='|', horizontal='-', intersection='+'):
    new_text_characters = []
    for char, cn, cs, cw, ce in zip(text, *neighbors(text)):
        new_char = ''
        if char == vertical:
            new_char = symbols['ns']
        elif char == horizontal:
            new_char = symbols['we']
        elif char == intersection:
            key = (('n' if cn in [intersection, vertical] else '') +
                   ('s' if cs in [intersection, vertical] else '') +
                   ('w' if cw in [intersection, horizontal] else '') +
                   ('e' if ce in [intersection, horizontal] else ''))
            new_char = symbols[key] if key else char
        else:
            new_char = char
        assert len(new_char) == 1
        new_text_characters.append(new_char)

    return ''.join(new_text_characters)


def main():
    print(ascii_to_box(unicode(sys.stdin.read(), encoding='utf-8')))

if __name__ == '__main__':
    main()

