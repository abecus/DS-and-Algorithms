
class Heap():
    
    sortedHeap = []

    def __init__(self, heap, heapType='max'):
        """
        type heap: a list for complete binary tree

        type heapType: max or min for heap type
        """
        self.heap = heap
        self.heapType = heapType

    def heapify(self, i):
        """
        Itype: index to the node (0 based)

        node = i

        leftChild = 2*i

        rightChild = 2*i+1

        parent = i//2
        """
        if self.heapType == "max":
            while i<len(self.heap)//2:
                """
                comparing childs and spawing max to its parent if it exist,
                and doing same on swaped child node (now were parent (opposing nature) is)
                else, return
                """
                try:      
                    if self.heap[(i+1)*2-1]>self.heap[(i+1)*2] and self.heap[(i+1)*2-1]>self.heap[i]:
                        self.heap[i], self.heap[(i+1)*2-1] = self.heap[(i+1)*2-1], self.heap[i]
                        i = (i+1)*2-1

                    elif self.heap[(i+1)*2-1]<self.heap[(i+1)*2] and self.heap[(i+1)*2]>self.heap[i]:
                        self.heap[i], self.heap[(i+1)*2] = self.heap[(i+1)*2], self.heap[i]
                        i = (i+1)*2

                    elif self.heap[(i+1)*2-1] == self.heap[(i+1)*2] and self.heap[(i+1)*2-1]>self.heap[i]:
                        self.heap[i], self.heap[(i+1)*2-1] = self.heap[(i+1)*2-1], self.heap[i]
                        i = (i+1)*2-1

                    else:
                        return

                except:
                    if self.heap[(i+1)*2-1]>self.heap[i]:
                        self.heap[i], self.heap[(i+1)*2-1] = self.heap[(i+1)*2-1], self.heap[i]
                        i = (i+1)*2-1

                    else:
                        return
            
        else:
            while i<len(self.heap)//2:
                """
                comparing childs and spawing min to its parent if it exist,
                and doing same on swaped child node (now were parent (opposing nature) is)
                else, return
                """
                try:      
                    if self.heap[(i+1)*2-1]<self.heap[(i+1)*2] and self.heap[(i+1)*2-1]<self.heap[i]:
                        self.heap[i], self.heap[(i+1)*2-1] = self.heap[(i+1)*2-1], self.heap[i]
                        i = (i+1)*2-1

                    elif self.heap[(i+1)*2-1]>self.heap[(i+1)*2] and self.heap[(i+1)*2]<self.heap[i]:
                        self.heap[i], self.heap[(i+1)*2] = self.heap[(i+1)*2], self.heap[i]
                        i = (i+1)*2

                    elif self.heap[(i+1)*2-1] == self.heap[(i+1)*2] and self.heap[(i+1)*2-1]<self.heap[i]:
                        self.heap[i], self.heap[(i+1)*2-1] = self.heap[(i+1)*2-1], self.heap[i]
                        i = (i+1)*2-1

                    else:
                        return

                except:
                    if self.heap[(i+1)*2-1]<self.heap[i]:
                        self.heap[i], self.heap[(i+1)*2-1] = self.heap[(i+1)*2-1], self.heap[i]
                        i = (i+1)*2-1

                    else:
                        return
                
    def buildHeap(self):
        '''
        Builds heap
        '''
        for i in reversed(range(len(self.heap)//2)):
            self.heapify(i)

    def insert(self, node):
        """
        Itype node: comaparable object

        inserts a node in heap 
        """
        self.heap.append(node)
        i = (len(self.heap))//2 - 1
        while i>0:
            self.heapify(i)
            i = i//2
        self.heapify(0)
    
    def delete(self):
        """
        rtype: int (root node)

        deletes root node from heap 
        """
        root = self.heap[0] 
        self.sortedHeap.append(root)
        self.heap[-1], self.heap[0] = self.heap[0], self.heap[-1] 
        self.heap = self.heap[:-1]
        self.heapify(0)
        return root

    def heapSort(self):
        """
        rtype: sorted heap in list

        deletes roots and append to the sortedHeap
        """
        for _ in range(len(self.heap)):
            self.delete() 
        return self.sortedHeap

    
if __name__ == "__main__":

    h1 = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1, 2, 3]
    heap = [10, 20, 15, 12, 40, 25, 18, 40]
    
    print(h1)
    a = Heap(h1, 'max')
    
    a.buildHeap()
    print('build', a.heap)

    a.insert(35)
    print('inserted', a.heap)

    a.delete()
    a.delete()
    print(a.heap)
    
