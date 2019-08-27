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
    dp = [0 if i==0 else float('inf') for i in range(val+1)]
    
    for i in range(1, val+1):
        for coin in coins:
            if i >= coin:
                dp[i]= min(dp[i-coin]+1, dp[i])
    
    return dp[val]

if __name__ == "__main__":
    coins = [20, 10, 5, 50, 100, 2, 1, 500, 1000] 
    val = 786
    print(minCoin(coins, val))
        