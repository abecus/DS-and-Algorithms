"""
_________________________693. Binary Number with Alternating Bits_________________________
Difficulty: Easy		Likes: 359		Dislikes: 74		Solution: Available
Total Accepted: 52.5K		Total Submission: 89.3K		Acceptance Rate: 58.8%
Tags:  Bit Manipulation


Given a positive integer, check whether it has alternating bits:
namely, if two adjacent bits will always have different values. 


Example 1:
Input: 5
Output: True

Example 2:
Input: 7
Output: False

Example 3:
Input: 11
Output: False

Example 4:
Input: 10
Output: True

"""


def hasAlternatingBits(n):
	s=bin(n)[2:]
	return all(s[i-1]!=s[i] for i in range(1,len(s)))

if __name__ == "__main__":
	n=12
	print(hasAlternatingBits(n,))
 
"""
similarQuestions::
		Number of 1 Bits: Easy
"""
