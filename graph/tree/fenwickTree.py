class FenwickTree:
	def __init__(self, arr):
		self.tree = [0]+arr.copy()
		self.createTree()

	def createTree(self)->None:
		"creates the fenwick tree from the arr in O(n)"
		for i in range(1, len(self.tree)):
			j=i+self.getLsb(i)
			if j<len(self.tree):
				self.tree[j]+=self.tree[i]

	@staticmethod
	def getLsb(n:int)->int:
		"return the 2^(position of LSB(n))"
		if n==0:	return 1
		c=1
		while not n&1:
			n>>=1
			c<<=1
		return c

	def prefixSum(self, index:int)->int:
		"equivalent to sum(arr[:index]) but in O(ln(index))"
		sum = 0
		while index:
			sum+=self.tree[index]
			index-=self.getLsb(index)
		return sum
 
	def rangeSum(self, leftIndex:int, rightIndex:int)-> int:
		"equivalent to sum(arr[leftIndex:rightIndex]) but in O(ln(rightIndex))"
		return self.prefixSum(rightIndex)-self.prefixSum(leftIndex)

	def update(self, index:int, value: int)-> None:
		"adds the value to given index but in O(ln(N))"
		index+=1
		while index<len(self.tree):
			self.tree[index]+=value
			index+=self.getLsb(index)


if __name__ == "__main__":
	import itertools, random
	arr=[*range(20)]
	random.shuffle(arr)
 
	f=FenwickTree(arr)
	# print(f.tree)
	
	# update test_____________
	# for i in range(10):
	# 	val=random.randint(10,50)
	# 	arr[i]+=val
	# 	f.update(i, val)
	# 	print([f.prefixSum(k) for k in range(1, len(arr)+1)]==[*itertools.accumulate(arr)])

	# range query Test________________
	for i in range(10):
		# updating values at an index
		val=random.randint(10,50)
		arr[i]+=val
		f.update(i, val)

		# random index st. idx1<idx2<=len(arr)
		idx1=random.randint(0,len(arr)//2 +1)
		idx2=random.randint(idx1+1, len(arr))

		print(f.rangeSum(idx1, idx2)==sum(arr[idx1:idx2]))