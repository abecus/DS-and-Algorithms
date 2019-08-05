import heapq

h = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1, 2, 3]
heapq.heapify(h)
print(f"heapyfied--> {h}")

print(f"pop and then add--> {heapq.heapreplace(h, 0)}")
print(f"add and then pop--> {heapq.heappushpop(h, -1)}")
print(f"5 largest elements--> {heapq.nlargest(5, h)}")
print(f"5 smallest elements--> {heapq.nsmallest(5, h)}")
