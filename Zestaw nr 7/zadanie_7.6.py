import itertools
import random
  
def iterator_a(iter_num):
    iterator_a = itertools.cycle([0, 1])

    for x in range(iter_num):
        if x < iter_num - 1:
            print(next(iterator_a), end=', ')
        else:
            print(next(iterator_a))

def iterator_b(iter_num):
    iterator_b = iter(lambda: random.choice(["N","E","S","W"]), 1)

    for x in range(iter_num):
        if x < iter_num - 1:
            print(next(iterator_b), end=', ')
        else:
            print(next(iterator_b))

def iterator_c(iter_num):
    iterator_c = itertools.cycle([0,1,2,3,4,5,6])

    for x in range(iter_num):
        if x < iter_num - 1:
            print(next(iterator_c), end=', ')
        else:
            print(next(iterator_c))

if __name__ == "__main__":
    iterator_a(20)
    iterator_b(20)
    iterator_c(20)
