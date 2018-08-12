#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumBribes function below.
def minimumBribes(q):
    number_bribes = 0
    posible_persons = [1, 2, 3]  # List of possibles next persons

    for position, person in enumerate(q, start=1):
        if person not in posible_persons:
            print("Too chaotic")
            break
        else:
            number_bribes += posible_persons.index(person)
            next_person = max(posible_persons) + 1
            posible_persons.remove(person)
            if next_person <= len(q):
                posible_persons.append(next_person)
    else:
        print(number_bribes)


if __name__ == '__main__':
    with open("input", "r") as file:
        t = int(file.readline().strip())

        for t_itr in range(t):
            n = int(file.readline().strip())

            q = list(map(int, file.readline().rstrip().split()))

            minimumBribes(q)
