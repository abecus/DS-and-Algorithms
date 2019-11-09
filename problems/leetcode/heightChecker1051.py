"""
_________________________1051. Height Checker_________________________
Difficulty: Easy		Likes: 87		Dislikes: 688		Solution: None
Total Accepted: 26.3K		Total Submission: 38.5K		Acceptance Rate: 68.4%
Tags:  Array


Students are asked to stand in non-decreasing order of heights for an annual photo.
Return the minimum number of students not standing in the right positions.  (This is the number of students that must move in order for all students to be standing in non-decreasing order of height.)
 
Example 1:

Input: [1,1,4,2,1,3]
Output: 3
Explanation: 
Students with heights 4, 3 and the last 1 are not standing in the right positions.

 
Note:

1 <= heights.length <= 100
1 <= heights[i] <= 100
"""


def heightChecker(heights):
    l = len(heights)
    return l-sum(i==j for i,j in zip(heights, sorted(heights)))


if __name__ == "__main__":
    heights = [1,1,4,2,1,3]
    print(heightChecker(heights,))


"""
"""
