"""
_________________________473. Matchsticks to Square_________________________
Difficulty: Medium		Likes: 379		Dislikes: 42		Solution: Available
Total Accepted: 28.3K		Total Submission: 77.2K		Acceptance Rate: 36.6%
Tags:  Depth-first Search


Remember the story of Little Match Girl? By now, you know exactly what matchsticks the little match girl has, please find out a way you can make one square by using up all those matchsticks. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.
 Your input will be several matchsticks the girl has, represented with their stick length. Your output will either be true or false, to represent whether you could make one square using all the matchsticks the little match girl has.
Example 1:

Input: [1,1,2,2,2]
Output: true

Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.


Example 2:

Input: [3,3,3,3,4]
Output: false

Explanation: You cannot find a way to form a square with all the matchsticks.


Note:

The length sum of the given matchsticks is in the range of 0 to 10^9.
The length of the given matchstick array will not exceed 15.

"""


def makesquare(nums):
    s = sum(nums)
    sideLength = s//4
    if s<4 or sideLength*4!=s:
        return False
    
    l = len(nums)

    from functools import lru_cache
    @lru_cache(None)
    def foo(s1=0,s2=0,s3=0,j=0,sideLength=sideLength,l=l):
        if s1==s2==s3==sideLength:
            return True
        for i in range(j,l):
            s1+=nums[i]
            if s1<=sideLength and foo(s1,s2,s3,j=i+1):
                return True
            s1-=nums[i]
            
            s2+=nums[i]
            if s2<=sideLength and foo(s1,s2,s3,j=i+1):
                return 1
            s2-=nums[i]
            
            s3+=nums[i]
            if s3<=sideLength and foo(s1,s2,s3,j=i+1):
                return 1
            s3-=nums[i]
            
    def helper(nums, side, count, l=l, done=0, s=s):
        if done: return True
        if side==0:
            side = s/4
            if count==0:
                done=1
                return True, 0, 0
            return True, side, count-1
        
        for i in range(l):
            l = len(nums)
            print(count, i, nums)
            temp = nums[i]
            nums.remove(temp)
            side-=temp

            a, side, count = helper(nums, side, count)
            if a:
                continue
            else:
                count=4
                nums.insert(i, temp)
                side+=temp
        else:
            return False


    # return helper(nums, side, count)
    if foo():
        return 1
    return 0
    
    

if __name__ == "__main__":
    nums = [1,1,2,2,2]  #1
    nums = [3,3,3,3,4] #0
    nums = [5,5,5,5,4,4,4,4,3,3,3,3] #1
    nums = [20,13,19,19,4,15,10,5,5,15,14,11,3,20,11] #1
    nums = [5969561,8742425,2513572,3352059,9084275,2194427,1017540,2324577,6810719,8936380,7868365,2755770,9954463,9912280,4713511]
    print(len(nums))
    print(makesquare(nums,))


"""
"""
