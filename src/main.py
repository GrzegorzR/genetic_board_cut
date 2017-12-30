from src.genetic.Population import Population
import numpy as np
import sys

from src.genetic.cross_functions import order_cross
from src.genetic.decode_functions import Decoder
from src.solution import fit_function, get_result, get_sizes
import matplotlib.pyplot as plt

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

    for i in range(1000):
        pop.calculate_fitness()
        pop.create_new_population()
        pop.crossing()
        pop.mutation()
        bests.append(pop.best_val)
        avg.append(np.mean(pop.avg))
    plt.plot(bests)
    plt.plot(avg)
    plt.show()
    print pop.best.genotype

def main():

    run_algorithm(0.01, 0.3)


if __name__ == "__main__":
    main()
