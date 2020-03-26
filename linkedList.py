#%%
class Node:
    def __init__(self, val, *args, **kwargs):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, *args, **kwargs):
        self.head = None

    def insert(self, nodeVal:object)->None:
        "inserts a object in linked list"
        if not self.head:
            self.head = Node(nodeVal)
            self.temp = self.head
        else:
            self.temp.next = Node(nodeVal)
            self.temp = self.temp.next
        
    def find(self, val:object, head:Node=None, prev:Node=None)->Node:
        """
        returns the previous node of node with val 
        if val is found in the linked-list
        """
        if head:
            if head.val != val:
                return self.find(val, head.next, head)
                
            else:
                return prev
        
        else:
            return None
                
    def delete(self, val:object)->None:
        
        if self.head.val == val:
            self.head = self.head.next
            return
        
        prev = self.find(val, head = self.head, prev = None) 
        
        if prev:
            if prev.next:
                prev.next = prev.next.next
                
            else:
                prev.next = None     
            
    def traverse(self)->None:
        "prints the nodes"
        def helper(head):
            if head:
                print(head.val)
                return helper(head.next)
        
        helper(self.head)
    
    def reverse(self)->None:
        "reverses the nodes in place"
        curr = self.head
        prev = None
        
        while curr!=None:
            next = curr.next
            curr.next = prev
            prev = curr        
            curr = next
        self.head = prev
        
if __name__ == "__main__":
    l = LinkedList()
    l.insert(2)
    l.insert(3)
    l.insert(4)
    l.insert(10)
    # l.find()
    # l.traverse()
    # l.reverse()
    # l.traverse()
    

#%%
