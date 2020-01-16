from math import ceil


class IndexedPriorityQueue:
	def __init__(self, arr):
		"""arr: (key: val)"""

		self.arrSize = len(arr)
		self.heapSize = self.arrSize
		self.values = arr
		# self.map = {arr[i]:i for i in range(self.arrSize)}

		# map for getting key of the value for given position in heap,
		# inverseMap[any index of element in heap (int)] -> key
		self.inverseMap = [*range(len(arr))]

		# map for getting where the given key exists in the heap
		# positionMap[key] -> index of element in heap
		self.positionMap = self.inverseMap.copy()

	@staticmethod
	def _getParentId(id):
		return ceil(id/2)-1

	@staticmethod
	def _getLeftChildId(id):
		return 2*id+1

	def doesKeyExists(self, key):
		return key<self.heapSize and self.values[key]!=None

	def isLess(self, a, b):
		"returns bool for a<b"
		return self.values[self.inverseMap[a]]<self.values[self.inverseMap[b]] 

	def swap(self, i, j):
		"""
		itype: 
		i-index (int) of inverseMap,

		j-index (int) of inverseMap
		"""
		self.positionMap[self.inverseMap[j]] = i
		self.positionMap[self.inverseMap[i]] = j
		self.inverseMap[j], self.inverseMap[i] = self.inverseMap[i], self.inverseMap[j]

	def sink(self, i):
		# goes from parent to the child (down)
		"""
		comparing children and spawing parent to min of children if exist,
		and doing same on swapped parent node
		"""
		while 1:
			leftChild = self._getLeftChildId(i)
			if leftChild+1<self.heapSize and self.isLess(leftChild+1, leftChild):	leftChild+=1
			if leftChild>=self.heapSize or self.isLess(i, leftChild):	break
			self.swap(leftChild, i)
			i=leftChild

	def swim(self, i):
		# does same as sink function but by going bottom to up in heap
		p = self._getParentId(i)
		while 0<=p<i:
			if not self.isLess(i, p):	break
			self.swap(i, p)
			i = p
			p = self._getParentId(i)

	def heapify(self):
		for i in reversed(range(self.heapSize//2)):
			self.sink(i)
 
	def insert(self, value:object)->None:
		self.values.append(value)
		self.positionMap.append(self.heapSize)
		self.inverseMap.append(self.heapSize)
		# if self.heapSize>1:
		self.swim(self.heapSize-1)

		self.heapSize+=1
		# self.arrSize += 1
		# self.map[value] = self.arrSize

	def _peekKey(self)->object:
		"returns min value's key in heap"
		return self.inverseMap[0]

	def peek(self)->object:
		"returns min value in heap"
		return self.values[self._peekKey()]

	def pop(self)->object:
		"returns min element from Array (heap)"
		value = self.peek()
		key = self._peekKey()
		self.__remove(key)
		# if not self.doesKeyExists(key):
		# 	del self.map[value]
		return value

	def __remove(self, idx:int)->None:
		"idx : index of original arr, of which value has to be updated"
		i = self.positionMap[idx]
		self.swap(i, self.heapSize-1)
		self.heapSize -= 1
		self.sink(i=i)
		self.swim(i=i)

		self.values[idx] = None	# put removed values None
		self.positionMap[idx] = -1
		self.inverseMap[-1] = -1

	def remove(self, idx:int)->None:
		"idx : index of original arr, of which value has to be updated"
		assert self.doesKeyExists(idx), "Key does not exists"

		i = self.positionMap[idx]
		self.swap(i, self.heapSize-1)
		self.heapSize -= 1
		self.sink(i=i)
		self.swim(i=i)

		# del self.map[self.values[idx]]
		self.values[idx] = float('inf')	# put removed values None
		self.positionMap[idx] = -1
		self.inverseMap[-1] = -1

	def update(self, idx:int, value:object)->None:
		"idx : index of original arr, of which value has to be updated"
		assert self.doesKeyExists(idx), "Key does not exists"
		i = self.positionMap[idx]
		self.values[i] = value
		self.swim(i)
		self.sink(i)

	def decreaseKey(self, idx:int, value:object)->None:
		"idx : index of original arr, of which value has to be updated"
		assert self.doesKeyExists(idx), "Key does not exists"
		if value < self.values[idx]:
			self.values[idx]=value
			self.swim(self.positionMap[idx])

	def increaseKey(self, idx:int, value:object)->None:
		"idx : index of original arr, of which value has to be updated"
		assert self.doesKeyExists(idx), "Key does not exists"
		if self.values[idx] < value:
			self.values[idx]=value
			self.sink(self.positionMap[idx])

	def printSorted(self):
		print([self.values[k] for k in self.inverseMap])

if __name__ == "__main__":
	# arr = [9,8,5,6,2,3,4,1]
	# arr = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1, 2, 3]
	# arr = [10, 20, 15, 12, 40, 25, 18, 40]
	# arr = [*range(10)][::-1]
	arr = [3,15,11,17,7,9,2,1,6,5,16,4]
	
	pq = IndexedPriorityQueue(arr)
	pq.heapify()
	pq.insert(2)
	pq.insert(100)

	pq.printSorted()
	
	print(pq.heapSize-1)
	pq.update(pq.heapSize-1, 1000)
	# print(pq.map)

	print(pq.pop())
	# print(pq.map)

	print(pq.pop())
	# print(pq.map)

	print(pq.pop())
	# print(pq.map)

	# pq.printSorted()
	pq.remove(1)

	print([pq.pop() for _ in range(pq.heapSize)])


	