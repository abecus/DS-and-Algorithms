def heapify(arr: list, *, i: int=None) -> None:

	def helper(i, n):
		# goes from parent to the child (down)
		"""
		comparing children and spawing parent to min of children if exist,
		and doing same on swapped parent node
		"""
		while i < nTillLastRow:
			ch1 = 2*i + 1
			if ch1+1 < n and arr[ch1] > arr[ch1+1]:	
				ch1 += 1

			if arr[ch1] < arr[i]:
				arr[i], arr[ch1] = arr[ch1], arr[i]
				i=ch1
			else:
				break

	nTillLastRow = len(arr)//2
	n = len(arr)
	helper(i, n) if i!=None else (helper(i, n)  for i in reversed(range(nTillLastRow)))

def heapPush(heapArr: list, val: int) -> None:
	"inserts the given element into the heap Array"
 
	heapArr.append(val)
	i = len(heapArr)-1
	while i > 0:
		parent = i-1 //2
		if heapArr[parent] > heapArr[i]:
			heapArr[parent], heapArr[i] = heapArr[i], heapArr[parent]
			i = parent
		else:		
			break

def heapPop(heapArr: list) -> "listElement":
	"returns min element from Array (heap)"
 
	heapArr[0], heapArr[-1] = heapArr[-1], heapArr[0]
	toReturn = heapArr.pop()
	heapify(heapArr, i=0) # relaxing
	return toReturn


if __name__ == "__main__":

	temp = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1, 2, 3]
	# temp = [10, 20, 15, 12, 40, 25, 18, 40]
	# temp = [9,8,5,6,2,3,4,1]

	heapify(temp)
	heapPush(temp, 0)
	print("temp", temp)
	
	print([heapPop(temp) for _ in range(len(temp))])

