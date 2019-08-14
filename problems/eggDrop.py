
def eggDrop(n, f):
    dp =  [[0 for _ in range(f+1)] for _ in range(n+1)]
    
    for i in range(n+1):
        dp[i][1] = 1
        
    for i in range(f+1):
        dp[1][i] = i
    
    for egg in range(2, n+1):
        for floor in range(2, f+1):
            dp[egg][floor] = float('inf')
            for x in range(1, floor+1):
                dp[egg][floor] = min(
                                    1 + max(dp[egg-1][x-1], dp[egg][floor-x]),
                                    dp[egg][floor]
                                    )
    
    return dp[n][f]

if __name__ == "__main__":
    print(eggDrop(2, 1000))    