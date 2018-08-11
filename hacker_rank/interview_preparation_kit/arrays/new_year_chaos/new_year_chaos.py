#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the minimumBribes function below.
def minimumBribes(q):
    number_bribes = 0
    for position, person in enumerate(q, start=1):
        if (position - person) < -2:
            print("Too chaotic")
            break
        elif position < person:
            number_bribes += person - position
        elif position + 2 < len(q):


    else:
        print(number_bribes)


if __name__ == '__main__':
    with open("input", "r") as file:
        t = int(file.readline().strip())

        for t_itr in range(t):
            n = int(file.readline().strip())

            q = list(map(int, file.readline().rstrip().split()))

            minimumBribes(q)
