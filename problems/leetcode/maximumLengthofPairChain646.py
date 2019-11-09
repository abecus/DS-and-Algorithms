"""
_________________________646. Maximum Length of Pair Chain_________________________
Difficulty: Medium		Likes: 627		Dislikes: 56		Solution: Available
Total Accepted: 41.7K		Total Submission: 84.2K		Acceptance Rate: 49.6%
Tags:  Dynamic Programming



You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.


Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion. 


Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.

Example 1:

Input: [[1,2], [2,3], [3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4]


Note:

The number of given pairs will be in the range [1, 1000].

"""


def findLongestChain(pairs):
    pairs.sort(key=lambda x:x[1])
    # print(pairs)
    if not pairs:
        return 0
    res = 1
    curr = pairs[0][1]
    for i in pairs:
        if curr<i[0]:
            res+=1
            curr=i[1]
    
    return res
                

if __name__ == "__main__":
    pairs = [[1,2],[1, 1],[2,3], [3,4], [4,9], [4,8],[5,6],[5,10]]
    pairs = [[1,2], [2,3], [3,4]]
    pairs = [[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]]
    print(findLongestChain(pairs,))


"""
similarQuestions::
        Longest Increasing Subsequence: Medium
        Increasing Subsequences: Medium
"""
