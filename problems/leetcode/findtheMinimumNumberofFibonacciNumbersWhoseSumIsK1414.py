"""
_________________________1414. Find the Minimum Number of Fibonacci Numbers Whose Sum Is K_________________________
Difficulty: Medium		Likes: 178		Dislikes: 23		Solution: None
Total Accepted: 10.6K		Total Submission: 17.4K		Acceptance Rate: 60.6%
Tags:  Greedy, Array


Given the number k, return the minimum number of Fibonacci numbers
whose sum is equal to k, whether a Fibonacci number could be used
multiple times. The Fibonacci numbers are defined as:  F1 = 1 F2 = 1
Fn = Fn-1 + Fn-2 , for n > 2. 
 It is guaranteed that for the given
constraints we can always find such fibonacci numbers that sum k.
   


Example 1:
Input: k = 7
Output: 2 
For k = 7 we can use 2 + 5 = 7.

Example 2:
Input: k = 10
Output: 2 

Example 3:
Input: k = 19
Output: 3 
 1 <= k <= 10^9
"""


import functools, itertools, operator, bisect, array, math 
import typing

# class Solution:
# 	fibs = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049]

# 	def findMinFibonacciNumbers(self, k: int) -> int:
# 		def foo(n, s):
# 			if n<0:     return math.inf
# 			if n==0:    return s
			
# 			for i in reversed(range(0, bisect.bisect(self.fibs, n))):
# 				temp = foo(n - self.fibs[i], s+1)
# 				if temp!=math.inf:
# 					return temp
# 			return -1
			
# 		return foo(k, 0)
	
class Solution:
	fibs = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049]
	def findMinFibonacciNumbers(self, k: int) -> int:
		count = 0
		while k >= 1:
			count += 1
			k -= self.fibs[bisect.bisect(self.fibs, k) - 1]
		return count
	
		
			


if __name__ == "__main__":
	k = 19

	s = Solution()
	print(s.findMinFibonacciNumbers(k))

"""
"""
