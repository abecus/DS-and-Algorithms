"""
_________________________754. Reach a Number_________________________
Difficulty: Medium		Likes: 538		Dislikes: 408		Solution: Available
Total Accepted: 20.6K		Total Submission: 56.4K		Acceptance Rate: 36.6%
Tags:  Math




You      are      standing      at     position     0     on     an     infinite
number line.  There is a goal at position target.



On    each    move,    you    can   either   go   left   or   right.      During
the n-th move (starting from 1), you take n steps.



Return the minimum number of steps required to reach the destination.





Example 1:
 Input: target = 3
 Output: 2
 On the first move we step from 0 to 1.
 On the second step we step from 1 to 3.

Example 2:
 Input: target = 2
 Output: 3
 On the first move we step from 0 to 1.
 On the second move we step  from 1 to -1.
 On the third move we step from -1 to 2.
	 Note:
 target will be a non-zero integer in the range [-10^9, 10^9].
"""


import functools, itertools, operator, bisect, array, collections, math
from typing import *

class Solution(object):
    def reachNumber(self, target):
        target = abs(target)
        k = 0
        while target > 0:
            k += 1
            target -= k

        return k if target % 2 == 0 else k + 1 + k%2


if __name__ == "__main__":
	s = Solution()
	print(s.reachNumber(2))


"""
"""
