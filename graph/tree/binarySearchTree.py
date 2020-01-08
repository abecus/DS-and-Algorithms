#%%
class Node():
    
    def __init__(self, value, left=None, right=None, parent=None):
      self.value = value
      self.left = left
      self.right = right 
      self.parent = parent
      
    def get(self):
        return self.value
           
    def __getHeight(self):
        
        if self.left and self.right:
            return 1 + max(self.left.getHeight(), self.right.getHeight())
        
        elif self.left:
            return 1 + self.left.getHeight()
        
        elif self.right:
            return 1 + self.right.getHeight()

        else:
            return 1
    def setParent(self, parent):
        self.parent = parent
        
    def getParent(self):
        return self.parent
        
    def __getSize(self):
        # gives number of nodes in tree
        if self.left and self.right:
            return 1 + self.left.getSize() + self.right.getSize()

        elif self.left:
            return 1 + self.left.getSize()

        elif self.right:
            return 1 + self.right.getSize()

        else:
            return 1


class BST():

    def __init__(self):
        """
        type heap: a list for a binary tree
        """
        self.root = None
        
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            
        else:
            node = Node(value)
            self.__insertInTree(self.root, node)
        
    def __insertInTree(self, currentNode, node):
        if node.value < currentNode.value:
            if currentNode.left:
                return self.__insertInTree(currentNode.left, node)
        
            else:
                currentNode.left = node
                node.setParent(currentNode)
                
        elif node.value > currentNode.value:
            if currentNode.right:
                return self.__insertInTree(currentNode.right, node)
            
            else:
                currentNode.right = node
                node.setParent(currentNode)
                
    def find(self, value):
        f = self.__findNode(self.root, value)
        if f:
            return True
        else:
            return False        
            
    def __findNode(self, currentNode, value):
        if currentNode != None:
            if currentNode.value == value:
                return currentNode
            
            elif value < currentNode.value:
                return self.__findNode(currentNode.left, value)
            
            else:
                return self.__findNode(currentNode.right, value)
        else:
            return False
                           
    def getMax(self, node=None):
        if node:
            curr_node = node
        else:
            #We go deep on the right branch
            curr_node = self.root
        if self.root:
            while curr_node.right:
                curr_node = curr_node.right
        return curr_node
    
    def getMin(self, node=None):
        if node:
            curr_node = node
        else:
            #We go deep on the right branch
            curr_node = self.root
        if self.root:
            while curr_node.left:
                curr_node = curr_node.left
        return curr_node
                
    def delete(self, value):
        return self.__del(value)
            
    def getHeight(self):
        return Node.getHeight(self.root)
    
    def getSize(self):
        return Node._getSize(self.root)
    
    def preOrder(self, curr_node=None):
        nodeList = []
        if curr_node==None:
            curr_node = self.root

        def helper(curr_node):
            if curr_node:
                nodeList.append(curr_node.value)
                if curr_node.left:
                    helper(curr_node.left)
                if curr_node.right:
                    helper(curr_node.right)
                
        helper(curr_node)
        return nodeList
    
    def postOrder(self, curr_node=None):
        nodeList = []
        if curr_node==None:
            curr_node = self.root

        def helper(curr_node):
            if curr_node:
                if curr_node.left:
                    helper(curr_node.left)
                if curr_node.right:
                    helper(curr_node.right)
                nodeList.append(curr_node.value)
                
        helper(curr_node)
        return nodeList
    
    def inOrder(self, curr_node=None):
        nodeList = []
        if curr_node==None:
            curr_node = self.root
        
        def helper(curr_node):
            if curr_node:
                if curr_node.left:
                    helper(curr_node.left)
                nodeList.append(curr_node.value)
                if curr_node.right:
                    helper(curr_node.right)
            
        helper(curr_node)
        return nodeList
    
    def levelOrder(self, curr_node=None):
        nodeList = []
        if curr_node==None:
            curr_node = self.root
        
        def bfs(root, i=0):
            if root:
                try: nodeList[i]
                except: nodeList.append([])        
                nodeList[i].append(root.value)
                if curr_node.left:
                    bfs(root.left, i+1)
                if curr_node.right:
                    bfs(root.right, i+1)
                  
        bfs(curr_node)
        return nodeList
        
    def __del(self, value):
        #Look for the node with that value
        node = self.__findNode(self.root, value)
        print('p', node.value)
        if node and self.root:
            #If it has no children
            if node.left is None and node.right is None:
                self.__changeParent(node, None)
                node=None
            # has only right child
            elif node.right and node.left==None:
                self.__changeParent(node, node.right)
            # has only left child
            elif node.left and node.right==None:
                self.__changeParent(node, node.left)
            #  has both children
            else:
                #Gets the max value of the left branch
                tmpNode = self.getMax(node.left)
                #Deletes the tmpNode
                self.delete(tmpNode.value)
                #Assigns the value to the node to delete and keeps tree structure
                node.value = tmpNode.value
    
    def __changeParent(self, node, withNode):
        if withNode:
            withNode.setParent(node.parent)
            
        if node.parent:     # if their is only one node in tree
            #If it's the Right Children
            if node.parent.right==node:
                node.parent.right = withNode
            else:
                #Else it's the left children
                node.parent.left = withNode

#%%         
if __name__ == "__main__":
    
    # l = [-3, 6]
    l = [1, 5,-1, 6, 8, 0, 5]
    bst = BST()

    for i in l:
        bst.insert(i)
    
    # print(bst.root.value)
    # print(bst.find(3), bst.find(7), bst.find(5))
    
    # print(bst.getHeight(bst.root))
    print(bst.postOrder(bst.root))
    print(bst.inOrder(bst.root))
    print(bst.preOrder(bst.root))
    print(bst.levelOrder(bst.root))
    
    
             
        
    


#%%

