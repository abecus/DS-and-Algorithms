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
        
    def preorder(self):
        l=[]
        if self:
            l = l + [self.value]
            
            if self.left:
                self.left.preorder()
            
            if self.right:
                self.right.preorder()
        else:
            return l
        
    def postorder(self):
        # l = []
        if self:
            if self.left:
                self.left.postorder()
            
            if self.right:
                self.right.postorder()
            
            print(self.value)
        # else:
        #     return l
        
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
    
    def preOrder(self, curr_node):
        nodeList = []
        if curr_node:
            nodeList = nodeList + self.preOrder(curr_node.left)
            nodeList.insert(0, curr_node.value) 
            nodeList = nodeList + self.preOrder(curr_node.right)
        return nodeList
    
    def postOrder(self, curr_node):
        nodeList = []
        if curr_node:
            nodeList = nodeList + self.postOrder(curr_node.left)
            nodeList = nodeList + self.postOrder(curr_node.right)
            nodeList.insert(0, curr_node.value) 
        return nodeList
    
    def inOrder(self, curr_node):
        nodeList = []
        if curr_node:
            nodeList.insert(0, curr_node.value)
            nodeList = nodeList + self.inOrder(curr_node.left)
            nodeList = nodeList + self.inOrder(curr_node.right)
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
            #  has both childrens
            else:
                #Gets the max value of the left branch
                tmpNode = self.getMax(node.left)
                #Deletes the tmpNode
                self.delete(tmpNode.value)
                #Assigns the value to the node to delete and keesp tree structure
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
    bst.root.postorder()
             
        
    


#%%

