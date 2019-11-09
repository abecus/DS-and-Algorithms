"""
_________________________456. 132 Pattern_________________________
Difficulty: Medium		Likes: 758		Dislikes: 47		Solution: Available
Total Accepted: 33.7K		Total Submission: 122.7K		Acceptance Rate: 27.5%
Tags:  Stack



Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such
that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.
Note: n will be less than 15,000.
Example 1:

Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.


Example 2:

Input: [3, 1, 4, 2]

Output: True

Explanation: There is a 132 pattern in the sequence: [1, 4, 2].


Example 3:

Input: [-1, 3, 2, 0]

Output: True

Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].

"""

def find132pattern(nums):
    if len(nums) < 3: return False
    n = len(nums)
    stack = []
    third = float('-inf')
    for i in iter(nums[::-1]):
        if i < third: return True
        while stack and i > stack[-1]:
            third = stack.pop()
        stack.append(i)
    return False

if __name__ == "__main__":
    # nums = [3,4,2,1]
    nums = [-1, 3, 2, 0]
    # nums = [1,2,3,4]
    # nums = [6,12,3,4,6,11,20]
    
    print(find132pattern(nums,))


"""
"""
