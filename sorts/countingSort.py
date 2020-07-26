import random, time
from typing import *
from heapq import merge
import quickSort, insertionSort
import math


def countingSort(arr: List[int]) -> List[int]:

    minimum, maximum = min(arr), max(arr)
    counter = [0]*(maximum - minimum + 1)

    for i in arr:
        # counting all elements of arr in counting array
        counter[i - minimum] += 1

    for i in range(1, len(counter)):
        # accumulating count values
        counter[i] += counter[i-1]

    result = [None]*len(arr)
    for i in arr:
        # getting index of element in result array
        # and putting their
        index = counter[i - minimum] - 1
        counter[i - minimum] -= 1
        result[index] = i

    return result


if __name__ == "__main__":
    # arr = [random.randint(5,50) for _ in range(10)]
    arr = [47, 30, 21, 19, 14, 27, 41, 13, 22, 39]
    print(countingSort(arr))