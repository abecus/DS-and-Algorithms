class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTreeFromArray:
    
    def __init__(self, array):
        from collections import deque
        
        self.head = self.leaf = TreeNode(array[0])
        i = 1
        kids = deque([self.leaf])
        
        while i<len(array) and kids:
            # does level order traversal
            node = kids.popleft()
            
            val = array[i]
            if val:
                # creates left node of given node
                node.left = TreeNode(val) 
                kids.append(node.left)
            i+=1
            
            val = array[i]
            if val:
                # creates right node of given node
                node.right = TreeNode(val) if val!='null' else None
                kids.append(node.right)
            i+=1
    
    def getRoot(self):  
        return self.head
    
    def traverse(self, root=None):
        self.tree = []
        if not root:
            root = self.head
        def helper(root=root):
            if root:
                self.tree.append(root.val)
                if root.left:   
                    helper(root.left)
                if root.right:  
                    helper(root.right)
        helper()
        return self.tree
           
            
if __name__ == "__main__":
    root = [5,3,6,2,4,None,8,1,None,None,None,7,9]
    # print(len(root))
    b = BinaryTreeFromArray(root)
    b.traverse()