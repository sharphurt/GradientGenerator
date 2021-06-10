from collections import namedtuple
from random import randint


class Color(namedtuple('Color', 'r g b')):
    def __str__(self):
        return f'#{"{0:x}".format(self.r)}{"{0:x}".format(self.g)}{"{0:x}".format(self.b)}'


def colors(count):
    return [Color(randint(0, 255), randint(0, 255), randint(0, 255)) for _ in range(0, count)]
