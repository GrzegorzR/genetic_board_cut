from os import listdir
from os import listdir
from os.path import isfile, join
from src.utils.consts import *

def test_solution(filename):
    sizes = get_sizes("../input/{}".format(filename))
    solution, full_area = get_solution("../output/{}".format(filename))
    try:
        assert len(sizes) == len(solution)
        check_sizes(sizes, solution)
        check_area(solution, full_area)
        check_not_outside(solution)
        check_collisions(solution)
    except Exception as e:
        print filename
        print(e)


def get_filenames():
    output_path = "../output"
    input_path = "../input"
    output_set = set([f for f in listdir(output_path) if isfile(join(output_path, f))])
    input_set = set([f for f in listdir(input_path) if isfile(join(input_path, f))])

    result = list(input_set & output_set)
    return result


def get_sizes(filename):
    with open(filename) as f:
        data = f.readlines()
    data = [i.split(" ") for i in data]
    data = [(int(i[0]), int(i[1])) for i in data]
    return data


def check_area(solution, full_area):
    result = 0
    for rect in solution:
        if rect[2] != -1:
            result += rect[0] * rect[1]
    if full_area != result:
        raise Exception("Wrong full area.")


def get_solution(filename):
    with open(filename) as f:
        data = f.readlines()
    full_area = int(float(data[0]))
    data = data[1:]
    data = [i.split(" ") for i in data]
    data = [(int(i[0]), int(i[1]), int(i[2]), int(i[3]), int(i[4])) for i in data]
    return data, full_area


def check_sizes(sizes, solution):
    for i in range(len(sizes)):
        if sizes[i] != (solution[i][0], solution[i][1]):
            raise Exception("Wrong sizes")


def check_not_outside(solution):
    valid_rects = [rect for rect in solution if not rect[2] == -1]

    for rect in valid_rects:
        if rect[-1]:
            rect_points = [rect[2], rect[3], rect[2] + rect[1], rect[3] + rect[0]]
        else:
            rect_points = [rect[2], rect[3], rect[2] + rect[0], rect[3] + rect[1]]
        for i in rect_points:
            if i < 0: raise Exception("Rectangle outside.")
        if rect_points[0] > XMAX or rect_points[2] > XMAX : raise Exception("Rectangle outside.")
        if rect_points[1] > YMAX or rect_points[3] > YMAX: raise Exception("Rectangle outside.")


def check_collisions(solution):
    valid_rects = [rect for rect in solution if not rect[2] == -1]
    rects_points = []
    for rect in valid_rects:
        if rect[-1]:
            rects_points.append([rect[2], rect[3], rect[2] + rect[1], rect[3] + rect[0]])
        else:
            rects_points.append([rect[2], rect[3], rect[2] + rect[0], rect[3] + rect[1]])

    for i in range(len(rects_points)):
        for j in range(len(rects_points)):
            if  i != j:
                collidate(rects_points[i], rects_points[j])


def collidate(r1, r2):
    hoverlaps = not ((r1[0] >= r2[2]) or (r1[2] <= r2[0]))
    voverlaps = not ((r1[1] >= r2[3]) or (r1[3] <= r2[1]))
    if hoverlaps and voverlaps:
        raise Exception("Collision detected")

def main():
    ids = get_filenames()
    for filename in ids:
        test_solution(filename)


if __name__ == "__main__":
    main()
