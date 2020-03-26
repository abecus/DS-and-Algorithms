
def threeSumClosest(l, s):
    length = len(l)
    
    if length<3:
        return -1
    
    l.sort()
    error = float('inf')    
    
    for i in range(length-1):
        left = i+1
        right = length-1
        
        while left<right:
            temp = l[i]+l[left]+l[right]
            
            if abs(temp-s) < error:
                error = abs(temp-s)
                sol = temp          
                
            if temp < s:
                left+=1
                
            elif temp > s:
                right -= 1
            
            else:
                return temp
        
    return sol
    
if __name__ == "__main__":
    l = [-1, 1, 2, 4]
    t = 1
    print(threeSumClosest(l, t))