from functools import cmp_to_key
import matplotlib.pyplot as plt 
from matplotlib.patches import Polygon 
import random

#________ Graham algorithm for convex hull runtime O(n*ln(n)) space O(|H|) ________________

def convexHull(arr):
    """
    itype: list of arr in tuples (x1, x2)
    rtype: list of tuples for arr on convex hull
    """
    
    lowLeft = (float('inf'), float('inf'))
        
    for i in range(len(arr)):
        if arr[i][1]<=lowLeft[1]:
            if arr[i][1]<lowLeft[1]:
                lowLeft=arr[i]
        
            else:
                lowLeft = min(arr[i], lowLeft, key=lambda x: x[0])
        
    
    def translatedCrossProd(p1, p2, origin=lowLeft):
        """
        finds the cross product of two vectos p1 and p2 with origin=origin
        its Negative if p1 is clockwise of p2 after translation.
        
        rtype: float
        """
        return (p2[0] - origin[0]) * (p1[1] - origin[1]) - (p1[0] - origin[0]) * (p2[1] - origin[1])
        
    def findHull(arr):
        """
        finds the convex hull points of all points
        
        rtype: list of tuples
        """
        arr.remove(lowLeft)
        arr.sort(key=cmp_to_key(translatedCrossProd))    
        
        hull = [lowLeft, arr[0], arr[1]]    # first 3 nodes must be their
        n = len(arr)
        i=2
    
        while i<n:
            while len(hull) > 1 and translatedCrossProd(arr[i], hull[-2], origin=hull[-1]) > 0:
                """
                keeps the pivot(origin) at current of hull and find
                the angle between second last node of hull and node in arr at 
                ith index w.r.t.. If val > 0 its ccw then remove the cuurrent node from hull
                do same thing on new current node in hull (the last node).
                after taose all steps append the last node at ith index to hull
                it's bit confussing so read https://en.wikipedia.org/wiki/Graham_scan
                """
                hull.pop()
            
            hull.append(arr[i])
            i+=1
            
        return hull
    
    def display(arr, hull):
        """
        displays the wrapped points
        """
        fig, ax1 = plt.subplots()
        arr.append(lowLeft) # because we have removed it first while computing the hull
         
        # all points
        x = [p[0] for p in arr]
        y = [p[1] for p in arr]
        ax1.plot(x, y, marker='*', color='b', linestyle='None')

        # hull points
        xy = list(zip([p[0] for p in hull], [p[1] for p in hull]))
        ax1.add_patch(Polygon(xy, closed=True, alpha=0.2))
        
        plt.title('Convex Hull')
        plt.show()
        
    hull = findHull(arr)
    return  display(arr, hull)
    
if __name__ == "__main__":

    l = []
    for _ in range(100):
        l.append((random.randint(-100, 100), random.randint(-100, 100)))
        
    convexHull(l)
