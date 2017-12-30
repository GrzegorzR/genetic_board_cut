from src.genetic.decode_functions import Decoder
from src.genetic.fit_function import fit_function


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


def save_rect_list_to_file(rect_list, order, sizes, output_file='../out.txt'):
    size = fit_function(rect_list)
    print size
    order = list(order)
    with open(output_file, 'w') as f:
        f.write(str(size) + '\n')
        for i in range(len(order)):
            f.write(rect_to_line(rect_list[order.index(i)], sizes[i]))



