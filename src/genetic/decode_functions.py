import random
import numpy as np
from src.utils.Rectangle import Rectangle, create_rectangle, outside_big_rect, collide
from src.utils.file_functions import get_sizes, save_rect_list_to_file
from src.utils.plot_solution import plot_solution


class Decoder:
    def __init__(self, rect_sizes):
        self.rect_sizes = rect_sizes

    def __call__(self, *args, **kwargs):
        return self.get_result(args[0], args[1])

    def get_result(self, rect_order, rect_rotation):
        rect_sizes = self.rect_sizes
        rectangles = []
        points_list = [[], [], []]
        rectangles.append(Rectangle(0., 0., 0. + rect_sizes[rect_order[0]][0],
                                    0. + rect_sizes[rect_order[0]][1]))

        points_list = update_points_list(points_list, rectangles[0])

        for i in rect_order[1:]:
            added = False
            for point in points_list[0] + points_list[1] + points_list[2]:
                if not added:
                    new_rectangle = create_rectangle(point, rect_sizes[i], rect_rotation[i])
                    collision = False
                    collision = collision or outside_big_rect(new_rectangle)
                    for rect in rectangles:
                        if not collision and rect:
                            collision = collision or collide(rect, new_rectangle)
                    if not collision:
                        rectangles.append(new_rectangle)
                        points_list = update_points_list(points_list, new_rectangle)
                        added = True
            if not added:
                rectangles.append(0)
        return rectangles


def update_points_list(points_list, rectangle):
    points_list[0].append((rectangle.xmax, rectangle.ymin))
    points_list[1].append((rectangle.xmin, rectangle.ymax))
    points_list[2].append((rectangle.xmax, rectangle.ymax))
    return points_list

if __name__ == "__main__":
    sizes = get_sizes()
    n = len(sizes)
    order = np.random.permutation(n)
    rotations = [int(random.choice([True, False])) for _ in range(n)]

    decoder = Decoder(sizes)

    rect_list = decoder(order, rotations)
    save_rect_list_to_file(rect_list, order, sizes)

    plot_solution()