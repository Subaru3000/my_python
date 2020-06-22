import numpy
from itertools import groupby

with open('temper.star.txt') as file:

    s = file.readlines()
    print(list(map(float, s)))
    llist = list(map(float, s))
    print(max(llist))
    print(min(llist))
    print(numpy.mean(llist))

    new_llist = [el for el, _ in groupby(llist)]
    print(len(new_llist))