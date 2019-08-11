negativeWeightDirectedGraph = {
                        "A":{"B":1, "E":2},
                        "B":{"C":3},
                        "C":{"D":2},
                        "D":{"F":2},
                        "E":{"F":3, "B":-2},
                        "F":{"B":-6, "C":-4}
                        }

projectsGraph = {'a':{'f':1},
                 'b':{'f':1},
                 'c':{'d':1},
                 'd':{'b':1, 'a':1},
                 'e':{},
                 'f':{}
                 }