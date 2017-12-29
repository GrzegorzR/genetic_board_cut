from math import sin, pi
from random import randint

from src.genetic.decode_functions import binary, gray
from src.genetic.Population import Population
import numpy as np
import sys

from src.genetic.cross_functions import order_cross
from src.solution import fit_function, get_result


def run_algorithm(p_cross, p_mut):
    pop_size = 20
    genotype_size = 22
    fit_fun = fit_function
    cross_fun = order_cross
    decode_fun = get_result
    bests = []
    avg = []

    pop = Population(pop_size, p_cross, p_mut,
                     genotype_size, decode_fun, fit_fun, cross_fun, plot=True)

    for i in range(100):
        pop.calculate_fitness()
        pop.create_new_population()
        pop.crossing()
        pop.mutation()
        bests.append(pop.best_val)
        avg.append(np.mean(pop.avg))


def main():
    p_ms = np.arange(0, 0.1, 0.01)
    p_cs = np.arange(0, 0.7, 0.1)
    run_algorithm(0.01, 0.3)


if __name__ == "__main__":
    main()
