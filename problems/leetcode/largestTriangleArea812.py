"""
_________________________812. Largest Triangle Area_________________________
Difficulty: Easy		Likes: 149		Dislikes: 868		Solution: Available
Total Accepted: 18.8K		Total Submission: 32.8K		Acceptance Rate: 57.3%
Tags:  Math


You have a list of points in the plane. Return the area of the
largest triangle that can be formed by any 3 of the points. 
 


Example:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2
The five points are show in the figure below. The red triangle is the largest.
Notes: 
3 <= points.length <= 50.No points will be duplicated.
 -50 <= points[i][j] <= 50.Answers within 10^-6 of the true value will be accepted as correct.
 
"""


def largestTriangleArea(points):

"""
This module solves LeetCode's problem 0812 Largest Triangle Area.
"""

from typing import List
from math import atan2, pi

Point = List[float]
Points = List[Point]

class Solution:
	"""
	This class allows to find the largest triangle in a cloud of points.
	"""
	@staticmethod
	def get_polar_angle(pole: Point, point: Point) -> float:
		"""
		Return polar angle: angle between polar axis and pole-to-point line.
		"""
		if point == pole:
			return float("-inf")  # So that if we sort by angle, pole is first

		delta_x = point[0] - pole[0]
		delta_y = point[1] - pole[1]

		polar_angle = atan2(delta_y, delta_x)  # -pi -> pi

		if polar_angle < 0:
			polar_angle += pi  # 0 -> 2pi

		return polar_angle

	@staticmethod
	def get_bottom_left_point(points: Points) -> Point:
		"""
		Return downmost point. If there are several, return the leftmost.
		"""
		bottom_left_point = [float("inf"), float("inf")]

		for point in points:
			is_lower = (point[1] < bottom_left_point[1])
			is_equally_low = (point[1] == bottom_left_point[1])
			is_to_the_left = (point[0] < bottom_left_point[0])

			if is_lower or (is_equally_low and is_to_the_left):
				bottom_left_point = point

		return bottom_left_point

	@staticmethod
	def get_triangle_area(point1: Point, point2: Point, point3: Point):
		"""
		Return triangle area given its vertices' coordinates.

		Formula: https://en.wikipedia.org/wiki/Triangle#Using_coordinates
		"""
		prod1 = (point1[0] - point3[0]) * (point2[1] - point1[1])
		prod2 = (point1[0] - point2[0]) * (point3[1] - point1[1])

		triangle_area = 1/2 * abs(prod1 - prod2)

		return triangle_area

	@staticmethod
	def is_left_turn(point1: Point, point2: Point, point3: Point):
		"""
		Return true if 1 -> 2 -> 3 is a left turn. Else, return false.

		To do so, we use a property of the cross product of two vectors: that
		if v1 x v2 is positive, then v2 is to the left of v1 - that is, it's a
		left turn. Otherwise, it's a right turn or the points are collinear.
		"""
		vector1 = (point2[0] - point1[0], point2[1] - point1[1])
		vector2 = (point3[0] - point2[0], point3[1] - point2[1])

		cross_product = vector1[0]*vector2[1] - vector2[0]*vector1[1]

		return cross_product > 0

	def get_convex_hull(self, points: Points) -> Points:
		"""
		Return points on convex hull using Graham's Scan.

		See Graham's Scan on Wikipedia for pseudocode:
		https://en.wikipedia.org/wiki/Graham_scan
		"""
		pole = self.get_bottom_left_point(points)

		points.sort(key=lambda point: self.get_polar_angle(pole, point))

		convex_hull: Points
		stack: Points
		convex_hull = stack = []

		for point in points:
			while len(stack) >= 2:
				triple = (stack[-2], stack[-1], point)
				if not self.is_left_turn(*triple):  # Right turn or collinear
					stack.pop()  # Because point can't be on convex hull
				else:
					break  # To append point to stack and move to next point
			stack.append(point)

		return convex_hull

	def largestTriangleArea(self,  # pylint: disable=invalid-name
							points: Points) -> float:
		"""
		Return area of largest triangle that can be made using given points.

		The largest triangle is part of the convex hull. So let's start by
		finding the points that make up the convex hull. Then, let's build
		all possible triangles with those points and see which is biggest.
		"""
		convex_hull = self.get_convex_hull(points)

		max_triangle_area = 0
		convex_hull_len = len(convex_hull)

		for idx1 in range(convex_hull_len):
			# Combine idx1 with every index to its right to avoid repeats
			for idx2 in range(idx1, convex_hull_len):
				# Combine idx2 with every index to its right to avoid repeats
				for idx3 in range(idx2, convex_hull_len):
					triple = (
						convex_hull[idx1],
						convex_hull[idx2],
						convex_hull[idx3]
					)
					triangle_area = self.get_triangle_area(*triple)
					max_triangle_area = max(max_triangle_area, triangle_area)

		return max_triangle_area

if __name__ == "__main__":
	points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
	print(largestTriangleArea(points,))


"""
similarQuestions::
		Largest Perimeter Triangle: Easy
"""
