"""
The set [1, 2, 3, ... , n] contains a total of n! unique permutations. List all the permutations for an integer n in lexicographical order and return the kth permutation in the sequence as a string. To build this string, concatenate decimal representations of permutation elements from left to right without any delimiters.

Example:

For n = 3 and k = 3, the output should be
permutationSequence(n, k) = "213".

The ordered list of possible permutations for 3! is:
  1) "123"
  2) "132"
  3) "213"
  4) "231"
  5) "312"
  6) "321"
The 3rd permutation in the lexicographically ordered sequence is "213".
"""


def factoradic(k, s):
    res = []
    for i in range(1, s+1):
        res.append(k%i)
        k = k//i
    return res
        
def permutationSequence(n, k):
    nums = list(range(1, n+1))
    idxs = factoradic(k-1, n)[::-1]
    res = []
    for idx in idxs:
        res.append(nums[idx])
        nums = nums[:idx] + nums[idx+1:]
    return "".join(map(str, res))
