"""
_________________________236. Lowest Common Ancestor of a Binary Tree_________________________
Difficulty: Medium		Likes: 3835		Dislikes: 173		Solution: Available
Total Accepted: 479K		Total Submission: 1.1M		Acceptance Rate: 45.5%
Tags:  Tree


Given a binary tree, find the lowest common ancestor (LCA) of two
given nodes in the tree. According to the definition of LCA on
Wikipedia: “The lowest common ancestor is defined between two nodes
p and q as the lowest node in T that has both p and q as descendants
(where we allow a node to be a descendant of itself).” Given the
following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]    


Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
 Note:
All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.
"""


import functools, itertools, operator, bisect, array 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def foo(root):
            if not root:    
                return None
            
            left = foo(root.left)
            right = foo(root.right)
            
            if root == p or root == q:
                return root
            
            if left != None and right != None:
                if left != right:
                    return root
                
                else:
                    return left
                
            return left if left != None else right
        
        res = foo(root)
        return res


if __name__ == "__main__":
	pass


"""
similarQuestions::
		Lowest Common Ancestor of a Binary Search Tree: Easy
		Smallest Common Region: Medium
"""
