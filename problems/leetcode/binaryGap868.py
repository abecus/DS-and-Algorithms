"""
_________________________868. Binary Gap_________________________
Difficulty: Easy		Likes: 175		Dislikes: 420		Solution: Available
Total Accepted: 31.5K		Total Submission: 52.4K		Acceptance Rate: 60.2%
Tags:  Math


Given a positive integer N, find and return the longest distance
between two consecutive 1's in the binary representation of
N. If there aren't two consecutive 1's, return 0.            


Example 1:
Input: 22
Output: 2
22 in binary is 0b10110.
In the binary representation of 22, there are three ones, and two consecutive pairs of 1's.
The first consecutive pair of 1's have distance 2.
The second consecutive pair of 1's have distance 1.
The answer is the largest of these two distances, which is 2.

Example 2:
Input: 5
Output: 2
5 in binary is 0b101.
Example 3:
Input: 6
Output: 1
6 in binary is 0b110.
Example 4:
Input: 8
Output: 0
8 in binary is 0b1000.
There aren't any consecutive pairs of 1's in the binary representation of 8, so we return 0.
 Note:
1 <= N <= 10^9
"""


def binaryGap(N):
	prev=-1
	m=0
	i=0
	while N:
		if N&1:
			if prev!=-1:
				m=max(m, i-prev)
			prev=i
		N>>=1
		i+=1
	return m

if __name__ == "__main__":
	N = 4
	print(binaryGap(N,))


"""
"""
