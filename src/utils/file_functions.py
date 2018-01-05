from src.genetic.fit_function import fit_function


def get_sizes(sizes_file='../maleplyty.txt'):
    with open(sizes_file) as f:
        data = f.readlines()
    data = [x.strip() for x in data]
    data = [x.split(' ') for x in data]
    for i, point in enumerate(data):
        data[i] = [float(j) for j in point]
    return data


def rect_to_line(rect, size, rotation):
    if rect:
        return '{} {} {} {} {}\n'.format(int(int(size[0])),
                                         int(int(size[1])),
                                         int(rect.xmin),
                                         int(rect.ymin),
                                         rotation)
    else:
        return '{} {} {} {} {}\n'.format(int(size[0]), int(size[1]), -1, -1, rotation)


def save_rect_list_to_file(rect_list, order, sizes, rotations, output_file='../out.txt'):
    size = fit_function(rect_list)
    print size
    order = list(order)
    with open(output_file, 'w') as f:
        f.write(str(int(size)) + '\n')
        for i in range(len(order)):
            f.write(rect_to_line(rect_list[order.index(i)], sizes[i], rotations[i]))


def save_rect_sizes_to_file(sizes, output_file):
    with open(output_file, 'w') as f:
        for size in sizes:
            f.write("{} {}\n".format(size[0], size[1]))

