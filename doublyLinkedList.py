
#%%
class Node:
    def __init__(self, val, *args, **kwargs):
        # for creating Node Instances
        self.val = val
        self.next = None
        self.prev = None
        
    # def __eq__(self0.val==other.val
    

class DoublyLinkedList:
    def __init__(self, *args, **kwargs):
        self.head = None
        self.length = 0
        
    def __len__(self):
        return self.length
    
    def insert(self, nodeVal):
        """ inserts the Node a the tail or at last """
        
        if not self.head:
            # if there is no head create one
            self.head = Node(nodeVal)
            self.temp = self.head
        
        else:
            # if head is there then link node to last
            node = Node(nodeVal)
            node.prev = self.temp
            self.temp.next = node
            self.temp = self.temp.next
        
        self.length+=1
        
    def find(self, val, head=None):
        """
        returns the previous node if value exists else returns None
        """
        if head==None:
            head=self.head
            
        while head:
            if head.val == val:
                return head
            head = head.next

        return 0
                
    def delete(self, val):
        """
        finds and deletes the node from linked list if it exists
        """
        node = self.find(val, head = self.head) 
        
        if node == 0:   
            # if "val" does not exists in list
            return

        if node.prev != None:
            # if its not first node in list
            node.prev.next = node.next
            node.prev = None
            node.next = None
            
        else:
            self.head = node.next
            
            if self.head != None:
                self.head.prev = None
                
        self.length-=1
        
    def reverse(self):
        """ 
        reversese the node in linked list and changes the 
        head with tail
        """
        
        # curr = self.head
        # prev = None
               
        # def helper(curr, prev, next):
        #     if curr==None:
        #         self.head = prev
        #         return
            
        #     next = curr.next
        #     curr.next = prev
        #     prev = curr        
        #     curr = next
        #     return helper(curr, prev, next)
        
        # helper(curr, prev, None) 

    def __repr__(self):
        temp=self.head
        s=""
        while temp:
            s+=f"{temp.val} "
            temp=temp.next
        return s
    
    def __iter__(self):
        # used for "for" loops or creating iterables
        temp=self.head
        while temp:
            yield temp
            temp=temp.next
        
    def __next__(self):
        # for "next()" operator 
        temp=self.head
        while temp:
            yield temp
            temp=temp.next      
        
    def __contains__(self, val):
        # used for "in" operator
        return self.find(val)!=0
    
    def __getitem__(self, index):
        # used for '[]' notation
        if index>=self.length:
            raise IndexError("index does not exist")
        
        temp=self.head
        while temp and index:
            temp=temp.next
            index-=1
        return temp

    def  __eq__(self, other):
        return self.__repr__()==other.__repr__()
            
#%%       
if __name__ == "__main__":
    l = DoublyLinkedList()
    l.insert(2)
    l.insert(2)
    l.insert(3)
    l.insert(4)
    l.insert(10)
    
    # print(len(l))
    
    l.delete(2)
    l.delete(4)
    l.delete(10)
    # l.delete(10)
    
    print(len(l))

    # print(2 in l)
    
    print(l)
    
    for i in range(len(l)):
        print(l[i].val)

    # for i in l:
    #     print(i.val)

    # a=iter(l)
    # print(next(a).val)
    # print(next(a).val)
    # print(next(a).val)
    # print(next(a).val)
    # print(next(a).val)
    