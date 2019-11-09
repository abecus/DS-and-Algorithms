"""
_________________________1027. Longest Arithmetic Sequence_________________________
Difficulty: Medium		Likes: 291		Dislikes: 18		Solution: None
Total Accepted: 16.1K		Total Submission: 31.7K		Acceptance Rate: 50.6%
Tags:  Dynamic Programming


Given an array A of integers, return the length of the longest arithmetic subsequence in A.
Recall that a subsequence of A is a list A[i_1], A[i_2], ..., A[i_k] with 0 <= i_1 < i_2 < ... < i_k <= A.length - 1, and that a sequence B is arithmetic if B[i+1] - B[i] are all the same value (for 0 <= i < B.length - 1).
 
Example 1:

Input: [3,6,9,12]
Output: 4
Explanation: 
The whole array is an arithmetic sequence with steps of length = 3.


Example 2:

Input: [9,4,7,2,10]
Output: 3
Explanation: 
The longest arithmetic subsequence is [4,7,10].


Example 3:

Input: [20,1,15,3,10,5,8]
Output: 4
Explanation: 
The longest arithmetic subsequence is [20,15,10,5].


 
Note:

2 <= A.length <= 2000
0 <= A[i] <= 10000

"""


def longestArithSeqLength(A):
    l = len(A)
    from collections import defaultdict
    dp  = [defaultdict(lambda: 1)]
    m = 2
    
    # essentially brute-force solution with memo
    for i in range(1, l):
        dp.append(defaultdict(lambda: 1))
        for j in range(i):
            a = dp[j].get(A[i]-A[j], 1) + 1
            m = max(m, a)
            dp[i][A[i]-A[j]] = a
    return m


if __name__ == "__main__":
    A = [3,6,9,12]
    # A = [9,4,7,2,10]
    print(longestArithSeqLength(A,))


"""
"""
