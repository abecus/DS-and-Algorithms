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
		return max((id-1)//2, 0)

	def _getMinChildId(self, id):
		# returns the child with min value if exists else returns -1
		minChild = -1
		leftChild = 2*id+1
		rightChild = min(self.heapSize, leftChild+2)
		for j in range(leftChild, rightChild):
			if self.isLess(j, id):
				minChild = id = j
		return minChild

	def doesKeyExists(self, key):
		return key<self.arrSize and self.values[key]!=None

	def isLess(self, a, b):
		"returns bool for a<b"
		if self.inverseMap[a]==-1 or self.inverseMap[b]==-1:	return 0
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

	def _peekKey(self)->object:
		"returns min value's key in heap"
		return self.inverseMap[0]

	def peek(self)->object:
		"returns min value in heap"
		return self.values[self._peekKey()]

	def sink(self, i):
		# goes from parent to the child (down)
		"""
		comparing children and spawing parent to min of children if exist,
		and doing same on swapped parent node
		"""
		child = self._getMinChildId(i)
		while child!=-1:
			self.swap(child, i)
			i=child
			child = self._getMinChildId(i)

	def swim(self, i):
		# does same as sink function but by going bottom to up in heap
		p = self._getParentId(i)
		while self.isLess(i, p):
			self.swap(i, p)
			i = p
			p = self._getParentId(i)

	def heapify(self):
		for i in reversed(range(self.heapSize//2)):
			self.sink(i)

	def push(self, value:object)->None:
		self.values.append(value)
		self.positionMap.append(self.arrSize)
		self.inverseMap.append(self.arrSize)
		# if self.heapSize>1:
		self.swim(self.heapSize)

		self.heapSize+=1
		self.arrSize+=1
		# self.map[value] = self.arrSize

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

		if self.heapSize==1:
			self.__init__([])
			return

		self.heapSize -= 1
		self.sink(i=i)
		self.swim(i=i)

		self.values[idx] = None	# put removed values None
		self.positionMap[idx] = -1
		self.inverseMap.pop()

	def remove(self, idx:int)->None:
		"idx : index of original arr, of which value has to be updated"
		assert self.doesKeyExists(idx), "Key does not exists"

		i = self.positionMap[idx]
		self.swap(i, self.heapSize-1)

		if self.heapSize==1:
			self.__init__([])
			return

		self.heapSize -= 1
		self.sink(i=i)
		self.swim(i=i)

		# del self.map[self.values[idx]]
		self.values[idx] = None	# put removed values None
		self.positionMap[idx] = -1
		self.inverseMap.pop()

	def update(self, idx:int, value:object)->None:
		"idx : index of original arr, of which value has to be updated"
		assert self.doesKeyExists(idx), "Key does not exists"
		i = self.positionMap[idx]
		self.values[idx] = value
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
		if self.values[idx]<value:
			self.values[idx]=value
			self.sink(self.positionMap[idx])

if __name__ == "__main__":
	# arr = [9,8,5,6,2,3,4,1]
	# arr = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1, 2, 3]
	# arr = [10, 20, 15, 12, 40, 25, 18, 40]
	arr = [*range(10)][::-1]
	# arr = [3,15,11,17,7,9,2,1,6,5,16,4]
	
	pq = IndexedPriorityQueue(arr)
	pq.heapify()
	# pq.push(2)
	# pq.push(-1)
	
	# pq.update(pq.arrSize-1, 100)
	# pq.update(pq.arrSize-2, -1)
	print([pq.pop() for _ in range(pq.arrSize)])