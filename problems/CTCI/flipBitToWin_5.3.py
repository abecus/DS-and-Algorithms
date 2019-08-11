
def flipBitToWin(num):   
    print(bin(num)[2:]) 
    if ~num==0:
        return 0
    
    globalmax = 1
    currentmax = 0
    previousmax = 0
    
    while num!=0:
        if num & 1 == 1:
            currentmax+=1
        elif num & 1 == 0:
            if num & 2 == 0:
                previousmax = 0
            else:
                previousmax = currentmax
            currentmax = 0
        
        globalmax = max(currentmax+previousmax+1, globalmax)
        num >>= 1
        print(currentmax, previousmax, globalmax)
    return globalmax

if __name__ == "__main__":
    print(flipBitToWin(1775))