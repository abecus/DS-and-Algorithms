negativeWeightDirectedGraph = {
                        "A":{"B":1, "E":2},
                        "B":{"C":3},
                        "C":{"D":2},
                        "D":{"F":2},
                        "E":{"F":3, "B":-2},
                        "F":{"B":-6, "C":-4}
                        }

projectsGraph = {'a':set(['f']),
                 'b':set(['f']),
                 'c':set(['d']),
                 'd':set(['b', 'a']),
                 'e':set(),
                 'f':set()
                 }

graph1 = {1:set([5]),
          5:set([16, 17]),
          12:set(),
          6:set([7]),
          7:set([11]),
          11:set([6]),
          4:set([0]),
          0:set([8]),
          8:set([4,14]),
          14:set([13,0]),
          13:set([0]),
          3:set([9]),
          9:set([2,15]),
          2:set([15]),
          15:set([10])
}