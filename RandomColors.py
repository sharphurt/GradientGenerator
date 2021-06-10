from collections import namedtuple
from random import randint

Color = namedtuple('Color', 'r g b')


def colors(count):
    return [Color(randint(0, 255), randint(0, 255), randint(0, 255)) for _ in range(0, count)]
