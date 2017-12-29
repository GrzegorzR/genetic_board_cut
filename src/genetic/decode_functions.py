
const_step = 3./pow(2.,22)

def binary(genotype):
    number = float(int(''.join([str(i) for i in genotype]), 2))
    return -1. + number*const_step

def xor(a, b):
    return str(int(bool(a) != bool(b)))

def gray(genotype):
    genotype = ''.join([str(i) for i in genotype])
    result = genotype[0]
    for i in range(1, len(genotype)):
        result += xor (int(result[-1]), int(genotype[i]))
    number = float(int(result, 2))
    return -1. + number * const_step
