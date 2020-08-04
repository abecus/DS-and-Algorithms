"""
_________________________309. Best Time to Buy and Sell Stock with Cooldown_________________________
Difficulty: Medium		Likes: 2469		Dislikes: 85		Solution: Available
Total Accepted: 144.1K		Total Submission: 309.1K		Acceptance Rate: 46.6%
Tags:  Dynamic Programming


Say you have an array for which the ith element is the price of a given
stock on day i. Design an algorithm to find the maximum profit. You may
complete as many transactions as you like (ie, buy one and sell one
share of the stock multiple times) with the following restrictions:
 You may not engage in multiple transactions at the same time (ie,
you must sell the stock before you buy again). After you sell your
stock, you cannot buy stock on next day. (ie, cooldown 1 day)  


Example:
Input: [1,2,3,0,2]
Output: 3 

"""


import functools
import itertools
import operator
import bisect
import array
import collections
from typing import *


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        maxProfit = collections.defaultdict(lambda: 0)
        bestEntry = -prices[0]  # max(-prices[j] + maxProfit[j-2] )
        for i in range(1, len(prices)):
            maxProfit[i] = maxProfit[i-1]
            maxProfit[i] = max(maxProfit[i], prices[i]+bestEntry)
            bestEntry = max(bestEntry, -prices[i]+maxProfit[i-2])
        return maxProfit[len(prices)-1]


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([1, 2, 3, 0, 2]))


"""
similarQuestions::
		Best Time to Buy and Sell Stock: Easy
		Best Time to Buy and Sell Stock II: Easy
"""
