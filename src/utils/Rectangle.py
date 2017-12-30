from collections import namedtuple

from src.utils.consts import *

Rectangle = namedtuple('Rectangle', 'xmin ymin xmax ymax')


def create_rectangle(point, size):
    return Rectangle(point[0],
                     point[1],
                     point[0] + size[0],
                     point[1] + size[1])


def collide(a, b):
    dx = min(a.xmax, b.xmax) - max(a.xmin, b.xmin)
    dy = min(a.ymax, b.ymax) - max(a.ymin, b.ymin)
    if (dx > 0) and (dy > 0):
        return True
    else:
        return False


def outside_big_rect(new_rectangle):
    return new_rectangle.xmax > XMAX or new_rectangle.ymax > YMAX