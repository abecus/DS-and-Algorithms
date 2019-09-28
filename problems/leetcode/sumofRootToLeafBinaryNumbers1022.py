"""
_________________________1022. Sum of Root To Leaf Binary Numbers_________________________
Difficulty: Easy		Likes: 173		Dislikes: 61		Solution: None
Total Accepted: 19.1K		Total Submission: 31.6K		Acceptance Rate: 60.4%
Tags:  Tree


Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.
Return the sum of these numbers.
 
Example 1:


Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

 
Note:

The number of nodes in the tree is between 1 and 1000.
node.val is 0 or 1.
The answer will not exceed 2^31 - 1.

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def sumRootToLeaf(root):






if __name__ == "__main__":
	root = [1,0,1,0,1,0,1]
	print(sumRootToLeaf(root,))


"""
"""
