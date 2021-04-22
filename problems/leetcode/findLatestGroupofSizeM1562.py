"""
_________________________1562. Find Latest Group of Size M_________________________
Difficulty: Medium		Likes: 239		Dislikes: 54		Solution: None
Total Accepted: 7.7K		Total Submission: 19.8K		Acceptance Rate: 38.7%
Tags:  Binary Search


Given  an  array  arr that  represents a permutation of numbers from 1 to n. You
have a binary string of size n that initially has all its bits set to zero.     
At  each  step  i (assuming  both  the  binary  string  and  arr  are 1-indexed)
from   1   to n,   the  bit  at  position arr[i] is  set  to 1.  You  are  given
an   integer m and   you   need   to   find  the  latest  step  at  which  there
exists  a  group  of  ones  of  length m.  A  group  of  ones  is  a  contiguous
substring of 1s such that it cannot be extended in either direction.            
Return   the   latest   step   at   which   there   exists   a   group  of  ones
of length exactly m. If no such group exists, return -1.                        
                                                                                
																				


Example 1:  Input: arr = [3,5,1,2,4], m = 1
 Output: 4
 Step 1: "00100", groups: ["1"]
 Step 2: "00101", groups: ["1", "1"]
 Step 3: "10101", groups: ["1", "1", "1"]
 Step 4: "11101", groups: ["111", "1"]
 Step 5: "11111", groups: ["11111"]
 The latest step at which there exists a group of size 1 is step 4.
 
Example 2:  Input: arr = [3,1,5,4,2], m = 2
 Output: -1
 Step 1: "00100", groups: ["1"]
 Step 2: "10100", groups: ["1", "1"]
 Step 3: "10101", groups: ["1", "1", "1"]
 Step 4: "10111", groups: ["1", "111"]
 Step 5: "11111", groups: ["11111"]
 No group of size 2 exists during any step.
  
Example 3:  Input: arr = [1], m = 1
 Output: 1
  
Example 4:  Input: arr = [2,1], m = 2
 Output: 2
     n == arr.length 1 <= n <= 10^5 1 <= arr[i] <= n All integers in arr are distinct.
 1 <= m <= arr.length  
"""


import functools, itertools, operator, bisect, array, collections 
from typing import * 

class Solution:
	def findLatestStep(self, arr: List[int], m: int) -> int:
		def find(x):
			while x!=par[x]:
				par[x] = par[par[x]]
				x = par[x]
			return x
		
		def union(x,y):
			nonlocal count
			
			px, py = find(x), find(y)
			if px==py:  return
			if size[px]==m: count-=1
			if size[py]==m: count-=1
				
			if size[px] > size[py]:    
				par[py] = par[px]
				size[px] += size[py]
				if size[px]==m: count+=1
				
			else:
				par[px] = par[py]
				size[py] += size[px]
				if size[py]==m: count+=1
					
		count = 0
		n = len(arr)+2
		par = list(range(n))
		size = [0]*n
		res = -1
		for i, el in enumerate(arr, 1):
			size[el] = 1
			if m==1:    count+=1
			if size[el-1]:   union(el, el-1)
			if size[el+1]:   union(el, el+1)
			if count>0:    res = i
			
		return res

class Solution:
	def findLatestStep(self, A, m):
		if m == len(A): return m
		length = [0] * (len(A) + 2)
		res = -1
		for i, a in enumerate(A):
			left, right = length[a - 1], length[a + 1]
			if left == m or right == m:
				res = i
			length[a - left] = length[a + right] = left + right + 1
		return res
		

		


if __name__ == "__main__":
	arr = [3,5,1,2,4]; m = 1

	s = Solution()
	print(s.findLatestStep(arr, m))


"""
"""
