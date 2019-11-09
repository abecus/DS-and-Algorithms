"""
_________________________897. Increasing Order Search Tree_________________________
Difficulty: Easy		Likes: 362		Dislikes: 365		Solution: Available
Total Accepted: 43.1K		Total Submission: 65.1K		Acceptance Rate: 66.1%
Tags:  Tree, Depth-first Search


Given a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.

Example 1:
Input: [5,3,6,2,4,None,8,1,None,None,None,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \ 
1        7   9

Output: [1,None,2,None,3,None,4,None,5,None,6,None,7,None,8,None,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9  
Note:

The number of nodes in the given tree will be between 1 and 100.
Each node will have a unique integer value from 0 to 1000.

"""

import sys
sys.path.append('tree/')
from  binaryTree import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


head = leaf = TreeNode(None)
def increasingBST(root):
    def helper(root=root):
        global leaf
        if root:
            if root.left:helper(root.left)
            
            root.left=None
            leaf.right=root
            leaf=leaf.right
            
            if root.right:helper(root.right)
    helper()
    return head.right

if __name__ == "__main__":
    def main():
        bt = BinaryTreeFromArray([5,3,6,2,4,None,8,1,None,None,None,7,9])
        head = bt.getRoot()
        ans = increasingBST(head)
        print(bt.traverse(ans))
    main()

"""
"""
