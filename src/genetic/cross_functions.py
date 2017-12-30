from random import randint
import random


def one_point_cross(ind1, ind2):
    genotype1 = ind1.genotype
    genotype2 = ind2.genotype
    cross_point = randint(1, len(genotype1) - 1)
    res1 = genotype1[0:cross_point] + genotype2[cross_point:]
    res2 = genotype2[0:cross_point] + genotype1[cross_point:]
    ind1.genotype = res1
    ind2.genotype = res2


def order_cross(in1, in2):
    ind1 = in1.genotype
    ind2 = in2.genotype
    size = min(len(ind1), len(ind2))
    a, b = random.sample(xrange(size), 2)
    if a > b:
        a, b = b, a

    holes1, holes2 = [True] * size, [True] * size
    for i in range(size):
        if i < a or i > b:
            holes1[ind2[i]] = False
            holes2[ind1[i]] = False

    temp1, temp2 = ind1, ind2
    k1, k2 = b + 1, b + 1
    for i in range(size):
        if not holes1[temp1[(i + b + 1) % size]]:
            ind1[k1 % size] = temp1[(i + b + 1) % size]
            k1 += 1

        if not holes2[temp2[(i + b + 1) % size]]:
            ind2[k2 % size] = temp2[(i + b + 1) % size]
            k2 += 1

    for i in range(a, b + 1):
        ind1[i], ind2[i] = ind2[i], ind1[i]

    return ind1, ind2


if __name__ == "__main__":

    print order_cross(range(10), list(reversed(range(10))))
