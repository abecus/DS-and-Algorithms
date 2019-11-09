"""
_________________________638. Shopping Offers_________________________
Difficulty: Medium		Likes: 405		Dislikes: 364		Solution: Available
Total Accepted: 24.1K		Total Submission: 48.3K		Acceptance Rate: 49.9%
Tags:  Dynamic Programming, Depth-first Search



In LeetCode Store, there are some kinds of items to sell. Each item has a price.


However, there are some special offers, and a special offer consists of one or more different kinds of items with a sale price.


You are given the each item's price, a set of special offers, and the number we need to buy for each item.
The job is to output the lowest price you have to pay for exactly certain items as given, where you could make optimal use of the special offers.


Each special offer is represented in the form of an array, the last number represents the price you need to pay for this special offer, other numbers represents how many specific items you could get if you buy this offer.

You could use any of special offers as many times as you want.
Example 1:

Input: [2,5], [[3,0,5],[1,2,10]], [3,2]
Output: 14
Explanation: 
There are two kinds of items, A and B. Their prices are $2 and $5 respectively. 
In special offer 1, you can pay $5 for 3A and 0B
In special offer 2, you can pay $10 for 1A and 2B. 
You need to buy 3A and 2B, so you may pay $10 for 1A and 2B (special offer #2), and $4 for 2A.


Example 2:

Input: [2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]
Output: 11
Explanation: 
The price of A is $2, and $3 for B, $4 for C. 
You may pay $4 for 1A and 1B, and $9 for 2A ,2B and 1C. 
You need to buy 1A ,2B and 1C, so you may pay $4 for 1A and 1B (special offer #1), and $3 for 1B, $4 for 1C. 
You cannot add more items, though only $9 for 2A ,2B and 1C.


Note:

There are at most 6 kinds of items, 100 special offers.
For each item, you need to buy at most 6 of them.
You are not allowed to buy more items than you want, even if that would lower the overall price.

"""


def shoppingOffers(price, special, needs):
    special.sort(key=lambda x: sum(x[:-1]))
    l = len(special)
    
    def possible(left, state=0):
        # returns is it possible to buy any special offer
        if state:
            return all((i-j)>=0 for i, j in zip(state, left))
        else:
            return any(all((i-j)>=0 for i, j in zip(state[:-1], left)) for state in special)   
    
    def getPrice(spec):
        return sum(i*p for i,p in zip(spec, price))
    
    def left(spec, needTo):
        return (i-j for i,j in zip(needTo, spec))
        
        
    m = 0
    from functools import lru_cache
    @lru_cache(None)
    def helper(leftToBuy):
        if not possible(leftToBuy):
            return getPrice(leftToBuy)
        
        tmp = [1]*l
        for i in range(l):
            tmp[i] = 0
            spec = special[i][:-1]
            if possible(leftToBuy, spec):
                a = getPrice(spec)+helper(left(spec, leftToBuy))
            
            tmp[i] = 1
            c = helper(tuple([0]*len(price)))+getPrice(leftToBuy)
            

                
        return min()




if __name__ == "__main__":
    price = [2,5]
    special = [[3,0,5],[1,2,10]]
    needs = [3,2]
    print(shoppingOffers(price,special,needs,))


"""
"""
