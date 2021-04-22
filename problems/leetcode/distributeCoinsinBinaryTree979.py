"""
_________________________979. Distribute Coins in Binary Tree_________________________
Difficulty: Medium		Likes: 1823		Dislikes: 68		Solution: Available
Total Accepted: 46.7K		Total Submission: 67.5K		Acceptance Rate: 69.1%
Tags:  Depth-first Search, Tree


Given   the   root   of   a   binary   tree   with   N   nodes,   each   node in
the tree has node.val coins, and there are N coins total.                       
In  one  move,  we may choose two adjacent nodes and move one coin from one node
to another.  (The move may be from parent to child, or from child to parent.)   
Return the number of moves required to make every node have exactly one coin.   
                                                                                
                                                                                
                                                                                


Example 1:  
 Input: [3,0,0]
 Output: 2
   
Example 2:  
 Input: [0,3,0]
 Output: 3
   
Example 3:  
 Input: [1,0,2]
 Output: 2
   
Example 4:  
 Input: [1,0,0,null,3]
 Output: 4
    Note:
  1<= N <= 100 0 <= node.val <= N     
"""


import functools, itertools, operator, bisect, array, collections 
from typing import * 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        
        def dfs(root, parent):
            if root==None:
                return
            
            if parent!=None:
                g[parent].append(root)
                g[root].append(parent)
                
            dfs(root.left, root)
            dfs(root.right, root)
            
        
        def distribute(root):
            st = [(root, 0)]
            seen = set()
            
            while st and root.val>1:
                
                # print([(v.val,c) for v,c in st])
                
                t = []
                
                for node, c in st:
                    seen.add(node)
                    
                    for adj in g[node]:
                        if adj in seen: continue
                        c += 1
                        if adj.val==0:
                            adj.val+=1
                            root.val-=1
                            self.cost += c
                        t.append((adj, c))
                        
                st = t.copy()
                      
        g=collections.defaultdict(list)
        dfs(root, None)
        self.cost = 0
        
        for k,vl in g.items():
            print(k.val, [v.val for v in vl])
            
        for node in g.keys():
            if node.val>1:
                distribute(node)
        
        return self.cost        


if __name__ == "__main__":
	# s=Solution()
  pass



"""
similarQuestions::
		Sum of Distances in Tree: Hard
		Binary Tree Cameras: Hard
"""
