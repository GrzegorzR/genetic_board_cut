from collections import namedtuple
import numpy as np

from plot import plot

Rectangle = namedtuple('Rectangle', 'xmin ymin xmax ymax')

ra = Rectangle(3., 3., 5., 5.)
rb = Rectangle(1., 1., 4., 3.5)
XMAX = 2800
YMAX = 2070


def colidate(a, b):
    dx = min(a.xmax, b.xmax) - max(a.xmin, b.xmin)
    dy = min(a.ymax, b.ymax) - max(a.ymin, b.ymin)
    if (dx > 0) and (dy > 0):
        return True
    else:
        return False


def update_points_list(points_list, rectangle):
    points_list[0].append((rectangle.xmax, rectangle.ymin))
    points_list[1].append((rectangle.xmin, rectangle.ymax))
    points_list[2].append((rectangle.xmax, rectangle.ymax))
    return points_list


def create_rectangle(point, size):
    return Rectangle(point[0],
                     point[1],
                     point[0] + size[0],
                     point[1] + size[1])


def outside_big_rect(new_rectangle):
    return new_rectangle.xmax > XMAX or new_rectangle.ymax > YMAX


def get_result(rect_sizes, rect_order):
    rectangles = []
    points_list = [[], [], []]
    rectangles.append(Rectangle(0., 0., 0. + rect_sizes[rect_order[0]][0],
                                0. + rect_sizes[rect_order[0]][1]))

    points_list = update_points_list(points_list, rectangles[0])

    for i in rect_order[1:]:
        added = False
        for point in points_list[0] + points_list[1] + points_list[2]:
            if not added:
                new_rectangle = create_rectangle(point, rect_sizes[i])
                collision = False
                collision = collision or outside_big_rect(new_rectangle)
                for rect in rectangles:
                    if not collision and rect:
                        collision = collision or colidate(rect, new_rectangle)
                if not collision:
                    rectangles.append(new_rectangle)
                    points_list = update_points_list(points_list, new_rectangle)
                    added = True
        if not added:
            rectangles.append(0)
    return rectangles


def get_sizes(sizes_file='../maleplyty.txt'):
    with open(sizes_file) as f:
        data = f.readlines()
    data = [x.strip() for x in data]
    data = [x.split(' ') for x in data]
    for i, point in enumerate(data):
        data[i] = [float(j) for j in point]
    return data


def rect_to_line(rect, size):
    if rect:
        return '{} {} {} {} {}\n'.format(int(rect.xmax - rect.xmin),
                                         int(rect.ymax - rect.ymin),
                                         int(rect.xmin),
                                         int(rect.ymin),
                                         0)
    else:
        return '{} {} {} {} {}\n'.format(int(size[0]), int(size[1]), -1, -1, 0)


def total_area(rect_list):
    result = 0
    for rect in rect_list:
        if rect:
            result += int(rect.xmax - rect.xmin) * int(rect.ymax - rect.ymin)
    return result

def fit_function(rect_list):
    return float(total_area(rect_list))

def save_rect_list_to_file(rect_list, order, sizes):
    size = fit_function(rect_list)
    order = list(order)
    with open('../out.txt', 'w') as f:
        f.write(str(size) + '\n')
        for i in range(12):
            f.write(rect_to_line(rect_list[order.index(i)], sizes[i]))


def main():
    sizes = get_sizes()
    # order = list(reversed(range(0,12)))
    # order = range(0, 12)
    order = [ 7,  3 , 8,  1,  2, 10, 11 , 0 , 6,  5,  9 , 4]

    rect_list = get_result(sizes, order)
    save_rect_list_to_file(rect_list, order, sizes)


if __name__ == "__main__":
    main()
    plot()
