
class SetStack:
	"A stack with set to check if a object (non-mutable) in the stack"
	def __init__(self):
		self.stack, self.set = [], set()

	def pop(self)->None:
		ele = self.stack.pop()
		self.set.remove(ele)
		return ele

	def append(self, ele: object)->None:
		if ele not in self.set:
			self.stack.append(ele)
			self.set.add(ele)

	def doesContains(self, ele: object)->bool:
		return ele in self.set

	def __len__(self)->int:
		return len(self.stack)