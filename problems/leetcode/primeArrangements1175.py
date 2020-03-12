"""
_________________________1175. Prime Arrangements_________________________
Difficulty: Easy		Likes: 71		Dislikes: 140		Solution: None
Total Accepted: 8.5K		Total Submission: 16.8K		Acceptance Rate: 50.5%
Tags:  Math


Return the number of permutations of 1 to n so that prime numbers
are at prime indices (1-indexed.) (Recall that an integer is prime
if and only if it is greater than 1, and cannot be written as a
product of two positive integers both smaller than it.) Since
the answer may be large, return the answer modulo 10^9 + 7.   


Example 1:Input: n = 5
Output: 12

Example 2:Input: n = 100
Output: 682289015
 1 <= n <= 100
"""

import bisect
def numPrimeArrangements(n):
	primes=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
	nPrimes=bisect.bisect(primes, n)
	mod=pow(10,9)+7
	def factorial(n):
		fact = 1
		for i in range(1,n+1): 
			fact=(fact*i)%mod
		return fact
	return (factorial(n-nPrimes)*factorial(nPrimes))%mod


if __name__ == "__main__":
	n = 100
	print(numPrimeArrangements(n,))


"""
"""
