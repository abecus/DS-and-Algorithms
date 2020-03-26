"""
_________________________733. Flood Fill_________________________
Difficulty: Easy		Likes: 713		Dislikes: 145		Solution: Available
Total Accepted: 83.8K		Total Submission: 158.6K		Acceptance Rate: 52.8%
Tags:  Depth-first Search



An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on.  Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:

Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.


Note:
The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
"""


def floodFill(image, sr, sc, newColor):
	def getDir(i,j):
		for a,b in zip(row,col):
			if 0<=a+i<n and 0<=b+j<m:
				yield a+i, b+j

	def filler(i,j,c):
		seen[i][j]=None
		for x,y in getDir(i,j):
			if image[x][y]==c and seen[x][y]!=None:
				filler(x,y,c)
				image[x][y]=newColor

	row=[0,0,1,-1]
	col=[1,-1,0,0]
	n,m=len(image), len(image[0])
	seen=image.copy()

	c=image[sr][sc]
	filler(sr,sc,c)
	image[sr][sc]=newColor
	return image



if __name__ == "__main__":
	image = [
			[0,0,0],
			[0,1,1]
	]
	sr = 1
	sc = 1
	newColor = 2
	print(floodFill(image,sr,sc,newColor,))


"""
similarQuestions::
		Island Perimeter: Easy
"""
