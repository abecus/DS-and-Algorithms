
#%%
class Node:
    def __init__(self, val, *args, **kwargs):
        # for creating Node Instances
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, *args, **kwargs):
        self.head = None
    
    def insert(self, nodeVal):
        """ inserts the Node a the tail or at last """
        
        if not self.head:
            # if there is no head creat one
            self.head = Node(nodeVal)
            self.temp = self.head
        
        else:
            # if head is there then link node to last
            self.temp.next = Node(nodeVal)
            self.temp = self.temp.next
        
    def find(self, val, head=None, prev=None):
        """
        returns the previous node if value exists
        else returs None
        """
        if head:
            if head.val != val:
                return self.find(val, head.next, head)
                
            else:
                return prev
        
        else:
            return None
                
    def delete(self, val):
        """
        finds and deletes the node from linked list if it exists
        """
        if self.head.val == val:
            self.head = self.head.next
            return
        
        prev = self.find(val, head = self.head, prev = None) 
        if prev:
            if prev.next:
                prev.next = prev.next.next
                
            else:
                prev.next = None     
            
    def traverse(self):
        """
        prints the node's value of linked list for head 
        to tail
        """
        def helper(head):
            if head:
                print(head.val)
                return helper(head.next)
        
        helper(self.head)
    
    def reverse(self):
        """ 
        reversese the node in linked list and changes the 
        head with tail
        """
        
        curr = self.head
        prev = None
               
        def helper(curr, prev, next):
            if curr==None:
                self.head = prev
                return
            
            next = curr.next
            curr.next = prev
            prev = curr        
            curr = next
            return helper(curr, prev, next)
        
        helper(curr, prev, None) 


#%%       
if __name__ == "__main__":
    l = LinkedList()
    l.insert(2)
    l.insert(3)
    l.insert(4)
    l.insert(10)
