import random
from copy import deepcopy
import numpy as np
from Individual import Individual


class Population:
    def __init__(self, pop_size, p_cross, p_mut,
                 genotype_size, decode_fun, fit_fun,
                 cross_fun, plot=False):
        self.population = [Individual(genotype_size, decode_fun, fit_fun, p_mut) for _ in range(pop_size)]
        self.p_cross = p_cross
        self.pop_size = pop_size
        self.cross_fun = cross_fun
        self.best_val = 0
        self.best_x = 0
        self.avg = []
        self.bests = []
        self.plot = plot

    def calculate_fitness(self):
        for ind in self.population:
            ind.calculate_fitness()

    def crossing(self):

        cross_size = int(self.pop_size * self.p_cross)
        if cross_size % 2:
            cross_size -= 1
        ind_to_cross = random.sample(range(self.pop_size), cross_size)
        pairs_to_cross = [[ind_to_cross[i], ind_to_cross[int(i + cross_size // 2)]] for i in range(cross_size // 2)]
        for pair in pairs_to_cross:
            self.cross_fun(self.population[pair[0]], self.population[pair[1]])

    def mutation(self):
        for ind in self.population:
            ind.mutate()

    def create_new_population(self):
        fit_array = np.array([ind.fit_val for ind in self.population])
        best_ind = max(fit_array)
        if best_ind > self.best_val:
            self.best_val = best_ind
            best_index = np.where(fit_array == best_ind)[0][0]
            self.best_x = self.population[best_index].get_x()

        self.bests.append(self.best_val)
        self.avg.append(sum(fit_array) / len(fit_array))

        # print  , self.best_x, self.best_val
        old_min = min(fit_array)
        old_range = max(fit_array) - old_min
        new_min = 0
        new_range = 1
        positive = np.array([float((n - old_min) / old_range * new_range + new_min) for n in fit_array])
        normalized = [float(i) / sum(positive) for i in positive]
        a = sum(normalized)
        new_pop_nums = [np.random.choice(range(self.pop_size), p=normalized) for i in range(self.pop_size)]
        new_pop = [deepcopy(self.population[i]) for i in new_pop_nums]
        self.population = new_pop
