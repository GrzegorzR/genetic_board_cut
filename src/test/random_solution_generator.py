from random import randint

from src.genetic.decode_functions import Decoder
from src.main import run_algorithm
from src.utils.consts import *
from src.utils.file_functions import get_sizes, save_rect_list_to_file, save_rect_sizes_to_file
from src.utils.plot_solution import plot_solution
import time


def generate_random_sizes_list():
    length = randint(30, 40)
    result = []
    up =  randint(1, 2000)
    down = randint(1, 2000)
    if up < down:
        up, down = down, up
    for i in range(length):
        result.append((randint(down, up),randint(down, up)) )
    return  result


def main():

    sizes = generate_random_sizes_list()
    order, rotations = run_algorithm(p_cross=0.4, p_mut=0.05, sizes = sizes)

    decoder = Decoder(sizes)
    case_id = str(int(time.time()))


    rect_list = decoder(order, rotations)
    sizes_filepath = "../input/{}.txt".format(case_id)
    output_filepath = "../output/{}.txt".format(case_id)
    save_rect_sizes_to_file(sizes, sizes_filepath)
    save_rect_list_to_file(rect_list, order, sizes, rotations, output_filepath)



if __name__ == "__main__":
    for i in range(200):
        resmain()
        plot_solution()
