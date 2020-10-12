from typing import *


def defaultComparator(a, b):
	return a < b


def sink(arr: List[object], idx: int, cmpFunction: Callable = defaultComparator):
	halfLength = len(arr) >> 1

	while idx < halfLength:
		leftChild = 1 + (idx << 1)

		if leftChild + 1 < len(arr) and \
				cmpFunction(arr[leftChild+1], arr[leftChild]):
			leftChild += 1

		if cmpFunction(arr[leftChild], arr[idx]):
			arr[leftChild], arr[idx] = arr[idx], arr[leftChild]
			idx = leftChild
		else:
			break


def swim(arr: List[object], idx: int, cmpFunction: Callable = defaultComparator):
	while idx > 0:
		parent = (idx - 1) >> 1
		if cmpFunction(arr[idx], arr[parent]):
			arr[parent], arr[idx] = arr[idx], arr[parent]
			idx = parent
		else:
			break


def heapify(arr: List[object], cmpFunction: Callable = defaultComparator) -> None:
	"""
	arr: list to heapify

	cmpFunction: function for two argument which returns true if 
									first arg is less than the second arg
	"""

	halfLength = len(arr) >> 1

	for i in reversed(range(halfLength)):
		sink(arr, i, cmpFunction)


def heapPush(arr: List[object], val: int, cmpFunction: Callable = defaultComparator) -> None:
	"""
	inserts the given element into the arr

	cmpFunction: function for two argument which returns true if 
									first arg is less than the second arg
	"""

	arr.append(val)
	swim(arr, len(arr)-1, cmpFunction)


def heapPop(arr: List[object], cmpFunction: Callable = defaultComparator) -> object:
	"""
	returns min element from Array (heap)

	cmpFunction: function for two argument which returns true if 
									first arg is less than the second arg
	"""

	arr[0], arr[-1] = arr[-1], arr[0]
	toReturn = arr.pop()
	sink(arr, 0, cmpFunction)
	return toReturn


if __name__ == "__main__":
	import random

	def func(x, y):	return not (x < y)

	temp = [random.randint(0, 10) for _ in range(10)]
	temp2 = temp.copy()

	heapify(temp, cmpFunction=func)

	# for _ in range(1000):
	#     el = random.randint(0, 10000000)
	#     heapPush(temp, el)
	#     temp2.append(el)

	# while temp:
	#     heapPop(temp)

	print([heapPop(temp, cmpFunction=func)
				for _ in range(len(temp))], sorted(temp2))
