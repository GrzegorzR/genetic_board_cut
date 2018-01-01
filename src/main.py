from src.genetic.fit_function import fit_function
from src.genetic.Population import Population
import numpy as np
import sys

from src.genetic.cross_functions import order_cross
from src.genetic.decode_functions import Decoder
import matplotlib.pyplot as plt

from src.utils.file_functions import get_sizes, save_rect_list_to_file
from src.utils.plot_solution import plot_solution


def run_algorithm(p_cross, p_mut):

    fit_fun = fit_function

    sizes = get_sizes()
    cross_fun = order_cross
    pop_size = 20
    genotype_size = len(sizes)
    decode_fun = Decoder(sizes)
    bests = []
    avg = []

    pop = Population(pop_size, p_cross, p_mut,
                     genotype_size, decode_fun, fit_fun, cross_fun, plot=True)

    for i in range(300):
        print i
        pop.calculate_fitness()
        pop.create_new_population()
        pop.crossing()
        pop.mutation()
        bests.append(pop.best_val)
        avg.append(np.mean(pop.avg))
    plt.plot(bests)
    plt.plot(avg)
    plt.show()
    print pop.best.genotype, pop.best.rotations
    return pop.best.genotype, pop.best.rotations

def main():

    order, rotations = run_algorithm(p_cross=0.4, p_mut=0.05)
    sizes = get_sizes()

    decoder = Decoder(sizes)

    rect_list = decoder(order, rotations)
    save_rect_list_to_file(rect_list, order, sizes, rotations)



if __name__ == "__main__":
    main()
    plot_solution()
