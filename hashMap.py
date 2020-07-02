class Node:
	# for creating Node Instances
	def __init__(self, key, item, *args, **kwargs):
  		# uses val attribute as key
		self.val = key
		self.item = item
		self.next = None
		
	# def __eq__(self, other):
	# 	return self.val==other.val
	
	# def __hash__(self):
	# 	return sum(ord(i for i in str(self.val)))

class LinkedList:
	def __init__(self, *args, **kwargs):
		self.head = None
		self.length = 0
		
	def __len__(self):
		return self.length
	
	def insert(self, key, item):
		""" 
  		inserts the Node at tail if key is not present
		there else update the item of that key
  		"""
		
		if not self.head:
			# if there is no head create one
			self.head = Node(key, item)
			# self.temp = self.head
		
		else:
			# if head is there then link node to last
			temp=self.head
			while temp:
				if temp.val==key:
					temp.item = item
					return
				if temp.next==None:
					temp.next=Node(key, item)
				else:
					temp=temp.next
		self.length+=1
		
	def find(self, val, head=None, prev=None):
		"""
		returns the previous node if value exists else returns None
		"""
		if head==None:
			head=self.head
			
		while head:
			if head.val == val:
				return prev
			prev, head = head, head.next

		return 0
				
	def delete(self, val):
		"""
		finds and deletes the node from linked list if it exists
		"""
		if self.head==None:	return
  
		if self.head.val == val:
			self.head = self.head.next
			self.length-=1
			return
		
		prevNode = self.find(val, head = self.head, prev=None) 
		
		if prevNode!=0:
			self.length-=1
			if prevNode.next.next:
				prevNode.next = prevNode.next.next
			else:
				prevNode.next=None
	
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

	def get(self, val):
		temp=self.head
		while temp:
			if temp.val==val:
				return temp
			temp=temp.next
			
class HashMap:
    # Hash Map only for integers, string and 
    # tuples with integers or strings
	def __init__(self):
		self.size=20
		self.map=[None]*self.size
  
	def discard(self, key):
		"""
		tries to delete node with key=="key"
		"""
		valHash = self.hash(key)
		ll = self.map[valHash]
		if ll==None:	return
		ll.delete(key)
	
	def hash(self, val):
		return sum(ord(i) for i in str(val)) % self.size

	def __setitem__(self, key, item):
		valHash = self.hash(key)
		if self.map[valHash]==None:
			self.map[valHash]=LinkedList()
		self.map[valHash].insert(key, item)

	def __contains__(self, key):
		valHash = self.hash(key)
		ll = self.map[valHash]
		if ll==None:	return False
		node = ll.get(key)
		if node:	return True
		return False

	def __repr__(self):
		s=[]
		for ll in self.map:
			if ll!=None:
				for node in ll:
					s.append(f"{node.val}:{node.item}")
		return "{"+", ".join(s)+"}"

	def __iter__(self):
		# used for "for" loops or creating iterables
		for ll in self.map:
			if ll!=None:
				for node in ll:
					yield node.val, node.item

	# def __next__(self):
	# 	# for "next()" operator 
	# 	temp=self.head
	# 	while temp:
	# 		yield temp
	# 		temp=temp.next      
		
	def __getitem__(self, key):
		# used for "in" operator
		valHash = self.hash(key)
		ll = self.map[valHash]

		if ll==None:
			raise KeyError("key does not exists")

		node = ll.get(key)

		if node:
			return node.item
		else:
			raise KeyError("key does not exists")
     
      
if __name__ == "__main__":
	h=HashMap()
	for i in range(10):
		h[i]=f"{i}"
  
	# for i in h:	
	# 	print(i)
 
	print(h)
	h[0]=100
	print(h)
	for i in range(1):
		h.discard(i)
	print(h)
		
