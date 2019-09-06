#%%
class Node:
    def __init__(self, val, *args, **kwargs):
        """
        adds a string to trie
        
        itype: string
        """
        self.val = val
        self.count = 0
        self.child = {}

#%%        
class Trie:
    """
    to create tree of strings and TODO "to do search of words 
    and to find the similar word and similar words count 
    which starts with same latters as input"
    """
    
    root = Node('*')
    
    def add(self, val):
        """
        adds a string to trie
        
        itype: string
        """
        if val:
            return self.__adder(val, self.root, len(val)-1)
    
    @staticmethod
    def __childVals(node):
        # for debugging
        return [key.val for key in node.child.keys()]
    
    @staticmethod
    def __findChild(val, node):
        # to return the Node address from node
        #  which corresponds to the val
        for key in node.child.keys():
            if key.val==val:
                return key
            
        return False    
    
    def __adder(self, val, node, length, i=0):
        # helper function for adding the value in tree
        char = val[i]
        # childs = self.__childVals(node)
        addr = self.__findChild(char, node)
        
        if length == i:
            # if its last character to add
            if not addr:
                node.count += 1
                temp = Node(char)
                node.child[temp] = 0
                #print(f'last {char} added in {self.__childVals(node)}')
                return False
            return True
        
        elif addr:
            # if char already in the childs
            #print(f'found {char} in {childs}')
            exist = self.__adder(val, addr, length, i+1)
            if not exist:
                node.count += 1
            return 
        
        else:
            # if char not in child na dnot last
            node.count += 1
            temp = Node(char)
            node.child[temp] = 0
            #print(f'{char} added in {self.__childVals(node)}')
            self.__adder(val, temp, length, i+1)
            return
    
    def printAll(self):
        """
        prints all the nodes values in tree in dfs manner
        """
        l = {}
        
        def dfs(node):
            for child in node.child.keys():
                if child not in l:
                    dfs(child)
                    l[child] = 0                
                    print(child.val)
                    
                    dfs(child)             
        return dfs(self.root)
    
    def search(self, val):
        return 
   
#%%    
if __name__ == "__main__":
    t = Trie()              
    t.add('ab')
    t.add('ab')
    t.add('ac')
    t.add('bc')
    t.printAll()


#%%
