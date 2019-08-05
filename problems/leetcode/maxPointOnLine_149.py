"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:
Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4

Example 2:
Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
"""

def foo(List):
    num = 2
    l = len(List)

    if l>2:
        for i in range(l):
            tempmax = {}
            maxNum = 1
            
            for j in range(i+1, l):
                
                if List[j][0] == List[i][0]:        # A special case for two points of same coordinates
                    
                    if List[j][1] == List[i][1]:
                        maxNum += 1 
                        
                    else:
                        tempmax["inf"] = 1
                    
                else:
                    temp = (List[j][1] - List[i][1]) / (List[j][0] - List[i][0])

                    if temp in tempmax:
                        tempmax[temp] += 1                                 
                    else:
                        tempmax[temp] = 1
                            
            if tempmax:   
                maxNum += max(tempmax.values())
            num = max(num, maxNum)
    else:
        return  l
    
    return num

if __name__ == "__main__":
    
    l0 = [[0,0],[0,0]]  # 2
    l1 = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]  # 4
    l2 = [[1,1],[2,2],[3,3]]    # 3
    l3 = [[0,0],[1,1],[0,0]]    # 3
    l4 = [[0,0],[1,1],[1,-1]]   # 2
    
    print(foo(l2))
