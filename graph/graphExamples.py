from graph import *


g1 = Graph()
g1.add(12, edgeType=0)
g1.add(4, [0], edgeType=1)
g1.add(8, [14, 4], edgeType=1)
g1.add(14, [13,0], edgeType=1)
g1.add(13, [0], edgeType=1)
g1.add(0, [8], edgeType=1)
g1.add(7, [6,11], edgeType=0)
g1.add(6, [7,11], edgeType=0)
g1.add(11, [7,6], edgeType=0)
g1.add(5, [17,16], edgeType=1)
g1.add(1, [5], edgeType=1)
g1.add(3,[9], edgeType=0)
g1.add(9,[15, 2], edgeType=0)
g1.add(2,[15], edgeType=0)
g1.add(15,[10], edgeType=0)
# print(g1.graph)

# ___________________________________________________
g2 = Graph()
g2.add("a", ["b", "c"], [1, 4])
g2.add("b", ["d", "c"], [5, 1])
g2.add("c", ["d", "b"], [3, 1])
g2.add("d", ["e", "g", "f"], [8, 9, 3])
g2.add("e", ["g"], [2])
g2.add("f", ["g"], [5])
# print(g2.graph)

# ________________________same g2 graph as g3
g3  = Graph()
g3.addFromDict("a", {"b":1,"c":4})
g3.addFromDict("b", {"d":5,"c":1})
g3.addFromDict("c", {"d":3,"b":1})
g3.addFromDict("d", {"e":8,"g":9, "f":3})
g3.addFromDict("e", {"g":2})
g3.addFromDict("f", {"g":5})
# print(g3.graph)

# ____________________________________________________
g4 = Graph()
g4.addFromDict("s", {"a":3,"b":5}, edgeType=0)
g4.addFromDict("a", {"d":3,"b":4}, edgeType=0)
g4.addFromDict("b", {"c":4}, edgeType=0)
g4.addFromDict("d", {"g":5}, edgeType=0)
g4.addFromDict("c", {"e":6}, edgeType=0)
# print(g4)

# ____________________________________________________
g5 = Graph()
g5.addFromDict("a", {"b":4, "d":5})
g5.addFromDict("b", {"c":4, "e":5})
g5.addFromDict("d", {"a":5, "e":2})
g5.addFromDict("e", {"b":5, "f":4, "d":2})
g5.addFromDict("f", {"g":3})
g5.addFromDict("s", {"a":3, "d":4})
# print(g5)