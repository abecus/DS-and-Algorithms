
def consecutiveOdds(arr):
    """
    finds the least increasing (by difference) consecutive odd sequence
    
    itype: arr
    rtype: int
    """ 
    dp = []
    
    for ele in arr:
        if ele%2==0:
            dp.append(-1)
        else:
            dp.append((ele, 1, 0))
    
    for i in range(1, len(dp)):
        # if previous and current entries are odd then 
        # accumulate the sum to current increase the 
        # count and update the difference
        prev = dp[i-1]
        curr = dp[i]
        if curr!=-1 and prev!=-1:
                dp[i] = (prev[0]+curr[0], prev[1]+1, prev[2]+abs(prev[0]-curr[0]))
         
    m = (float('inf'), float('inf'), float('inf'))
    # m as (sum, count, difference)
    i = len(dp)-1
    while i>=0:
        if dp[i]!=-1:
            # take minimum by difference i.e. dp[i][-1]
            m = min(dp[i], m, key=lambda x:x[-1])
            
            # and go back to one less than end of sequence
            i-=dp[i][1]
        
        else:
          i-=1
            
    return m[0]//m[1]
                
            
if __name__ == "__main__":
    
    arr = [3,36,36,62,121,65,21,370,660,6]
    print(consecutiveOdds(arr))
    