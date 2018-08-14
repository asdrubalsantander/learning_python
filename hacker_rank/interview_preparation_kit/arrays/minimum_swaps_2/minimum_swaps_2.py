#!/bin/python3

import math
import os
import random
import re
import sys
import time


# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    count_swaps = 0
    for position, number in enumerate(arr):
        smallest_number = min(arr[position:])
        if number != smallest_number:
            smallest_index = arr.index(smallest_number)
            arr[position], arr[smallest_index] = arr[smallest_index], arr[position]
            count_swaps += 1

    return count_swaps


if __name__ == '__main__':
    with open("input", "r") as file:
        n = int(file.readline().strip())
        arr = list(map(int, file.readline().rstrip().split()))

    start = time.time()

    res = minimumSwaps(arr)
    print(res)

    end = time.time()
    print(end - start)
