import random, time
from typing import *
from heapq import merge
import quickSort, insertionSort, countingSort
import math


def first_n_digits(num, n):
	return num // 10 ** (int(math.log(num, 10)) - n + 1)

def getLastDigit(x):
	return x%10

def bucketSort(arr: List[int]) -> None:
	"""
	only integer values are allowed
	
	itype: list
	rtype: list
	"""
	bucket = [[] for _ in range(9)]

	for i in arr:
		# store each element by their last digit
		# bucket[getLastDigit(i)].append(i)
		bucket[first_n_digits(i, 1) - 1].append(i)
		
	# for collection in bucket:
	#     # sort each bucket
	#     quickSort.quickSort(collection)
	#     # insertionSort.insertionSort(collection)

	for i in range(len(bucket)):
		# sort each bucket
		bucket[i] = countingSort.countingSort(bucket[i])

	# if all numbers have same number of digits there is no need 
	# for merge method just join the bucket is there order

	# merge the buckets
	return [*merge(*bucket)]

if __name__ == "__main__":
		
	a = [random.randint(1, 100) for _ in range(int(10e3))]
	print(bucketSort(a))    
							  