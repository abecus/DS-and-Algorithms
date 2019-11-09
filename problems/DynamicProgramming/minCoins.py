"""
Given a value V, if we want to make change for V cents, and
we have infinite supply of each of C = { C1, C2, .. , Cm} 
valued coins, what is the minimum number of coins to make the change?

Input: coins[] = {25, 10, 5}, V = 30
Output: Minimum 2 coins required
We can use one coin of 25 cents and one of 5 cents 

Input: coins[] = {9, 6, 5, 1}, V = 11
Output: Minimum 2 coins required
We can use one coin of 6 cents and 1 coin of 5 cents
"""

def minCoin(coins, val):
    dp = [float('inf') for _ in range(val+1)]
    dp[0] = 0
    
    for i in range(1, val+1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i-coin]+1, dp[i])
    
    return dp[val]


def minCoinRec(coins, val):
    from functools import lru_cache
    
    @lru_cache(None)
    def helper(v=val):
        if v==0:
            return 0
        
        try:   return min(helper(v-coin)+1 for coin in coins if coin<=v)
        except:     return float('inf')
    
    res=helper()
    print(helper.cache_info())
    return res if res!=float('inf') else -1

if __name__ == "__main__":
    coins = [20, 10, 5, 50, 100, 2, 500, 1000] 
    val = 3
    
    coins = [20, 10, 5, 50, 100, 2, 1, 500, 1000] 
    val = 786
    
    # coins = [9, 6, 5, 1] 
    # val = 11
    
    # coins= [1, 2]
    # val=3
    
    # coins= [2]
    # val=3
    
    # coins = [186,419,83,408]
    # val = 6249
    
    print(minCoin(coins, val))
    print(minCoinRec(coins, val))
             