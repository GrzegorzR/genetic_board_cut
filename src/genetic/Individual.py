import random
import numpy as np

class Individual:

    def __init__(self, genotype_size, decode_fun, fit_fun, p_mut):
        self.genotype = np.random.permutation(genotype_size)
        self.genotype_size = genotype_size
        self.decoder = decode_fun
        self.fit_fun = fit_fun
        self.p_mut = p_mut
        self.fit_val = None

    def mutate(self):
        if self.p_mut > random.random():
            i = random.randint(0, self.genotype_size - 1)
            j = random.randint(0, self.genotype_size - 1)
            self.genotype[i], self.genotype[j] = self.genotype[j], self.genotype[i]

    def calculate_fitness(self):
        self.fit_val = self.fit_fun(self.decoder(self.genotype))

    def get_x(self):
        return self.decoder(self.genotype)
