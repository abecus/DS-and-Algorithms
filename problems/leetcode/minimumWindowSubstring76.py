"""
_________________________76. Minimum Window Substring_________________________
Difficulty: Hard		Likes: 4605		Dislikes: 318		Solution: Available
Total Accepted: 405K		Total Submission: 1.2M		Acceptance Rate: 34.5%
Tags:  Hash Table, Sliding Window, String, Two Pointers


Given a string S and a string T, find the minimum window in S
which will contain all the characters in T in complexity O(n). 


Example:
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:
If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

"""


import functools, itertools, operator, bisect, array, math, collections

class QSet():
	def __init__(self, *args, **kwargs):
		self.s = collections.defaultdict(int)
		self.q = collections.deque()

	def push(self, x):
		for i in x:
			self.s[i]+=1
			self.q.append(i)

	def pop(self):
		last = self.q.popleft()
		if self.s[last]==1:
			del self.s[last]
		else:
			self.s[last]-=1
		return last

	def contains(self, t):
		return all(self.s[i]>0 for i in t)
	

class Solution:
	def minWindow(self, s: str, t: str) -> str:

		def isin(q, t):
			return all(q[i]-t[i]>=0 for i in t.keys())

		res = ''
		size = math.inf
		i = 0
		
		t = collections.Counter(t)
		q = collections.Counter()

		for j in range(len(s)):
			el = s[j]
			q[el] += 1

			while isin(q, t):
				if size > j-i+1:
					res = s[i : j+1]
					size = j-i+1


				last_el = s[i]
				i+=1

				if q[last_el] == 1:
					del q[last_el]

				else:
					q[last_el]-=1
			
		return "".join(res)

if __name__ == "__main__":
	S = "ADOBECODEBANC"
	T = "ABC"

	S = "a"
	T = "aa"

	s = Solution()
	print(s.minWindow(S, T))


"""
similarQuestions::
		Substring with Concatenation of All Words: Hard
		Minimum Size Subarray Sum: Medium
		Sliding Window Maximum: Hard
		Permutation in String: Medium
		Smallest Range Covering Elements from K Lists: Hard
		Minimum Window Subsequence: Hard
"""
