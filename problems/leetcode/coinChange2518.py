"""
_________________________518. Coin Change 2_________________________
Difficulty: Medium		Likes: 991		Dislikes: 40		Solution: None
Total Accepted: 60.4K		Total Submission: 135.4K		Acceptance Rate: 44.6%
Tags:  


You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.


 
Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:

Input: amount = 10, coins = [10] 
Output: 1

 
Note:
You can assume that

0 <= amount <= 5000
1 <= coin <= 5000
the number of coins is less than 500
the answer is guaranteed to fit into signed 32-bit integer

"""


count = 0
def change(amount, coins):
    
    # from array import array
    # dp = array('i', [0]*(amount+1))
    dp = [0 for _ in range(amount+1)]
    dp [0] = 1
    for c in coins:
        for i in range(c, amount+1):
            dp[i] += dp[i-c]
            
    return dp[-1]
    
    
if __name__ == "__main__":
    amount = 5
    coins = [1,2,5] #4
    print(change(amount,coins,))

"""
"""
