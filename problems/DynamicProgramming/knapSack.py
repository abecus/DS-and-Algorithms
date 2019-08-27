
def knapSack(val, wt, W):
    dp = [[0 for _ in range(W+1)] for _ in range(len(wt))]
    
    for i in range(len(wt)):
        for j in range(W+1):
            if wt[i]<=j:
                dp[i][j] = max(val[i]+dp[i-1][j-wt[i]], dp[i-1][j])
            else:
                dp[i][j]=dp[i-1][j]
    
    return dp[i][j], dp
    
if __name__ == "__main__":
    val  = [7,2,4,5]
    wt = [3,1,2,4]
    # val = [1,2,4,5]
    # wt = [1,2,4,5]
    W = 6
    print(knapSack(val,wt, W))