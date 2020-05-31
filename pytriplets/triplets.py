import time, cProfile
from math import sqrt
import math
import itertools

def pythagorean_triplet(n):
	s2 = time.perf_counter()
	count=0
	for b in range(n):
		for a in range(1, b):
			c = sqrt( a * a + b * b)
			if c % 1 == 0 and c<=n:
				# print(a, b, c)
				count+=1

	print(round(time.perf_counter()-s2, 4))
	print(count)


# primeFactor

def pow1(n):
	if not n:	return 0
	if n&1: return (pow1(n>>1)<<2) + ((n>>1)<<2) + 1
	else:	return (pow1(n>>1)<<2)
	
def pythagoreanTriplet(n):
	# res=[]
	s1 = time.perf_counter()
	count = 0
 
	firstStart = 4
	firstEnd = (n - int(sqrt((n<<1) -1)))<<1
	# firstEnd = (int(n/(1+sqrt(2)))+1)<<1
	# firstEnd = (int(0.5 * ((n<<1)+1 -sqrt((2*n*n) -1) +1)))<<1
	# firstEnd = (int(sqrt((2*n*n)+(2*n)+1)-n)+1)<<1

	for b2 in range(firstStart, firstEnd, 2):		# n-3+1
		secondStart = int(sqrt(b2))& ~1
		secondEnd = int(sqrt(b2*((b2>>1)-1)))+1
		# print(' ')
		for i in range(secondStart, secondEnd, 2):
			# print(i)
			sqVal = i*i
			q=sqVal//b2
			if q+i+(b2>>1)>n:
				break
			# print(sqVal/b2 +i, -((sqVal/b2)- b2//2), (b2>>1), sqVal/b2 +i+(b2>>1))
			if not sqVal%b2:
				x=q+i
				if x+(b2>>1)<=n:
					# print("\tThis-> ", x, (b2>>1)+i, x+(b2>>1))
					# res.append((x, (b2>>1)+i))
					count+=1
	print(round(time.perf_counter()-s1, 4))
	print(count)
	# return res


def pythagoreanTriplet2(n):
	s1 = time.perf_counter()
	count = 0
 
	firstStart = 4
	firstEnd = (2*n +1 -int(sqrt(2*n*n -1)))+1

	for b2 in range(firstStart, firstEnd, 2):
		secondStart = int(sqrt(b2))& ~1
		secondEnd = int(sqrt(2)* (b2>>1))+1
		for i in range(secondStart, secondEnd, 2):
			sqVal = i*i
			if not sqVal%b2:
				x = sqVal//b2 +i
				if x+(b2>>1)<=n:
					# print("This-> ", x, (b2>>1)+i, x+(b2>>1))
					# yield x, (b2>>1)+i, x+(b2>>1)
					count+=1
				
	print(round(time.perf_counter()-s1, 4))
	print(count)


if __name__ == "__main__":
	n=100		
	#1_000---881,  10_000---12471,  100---52, 100_000----161436, 1_000_000---1980642, 10_000_000---23471475
	
	# cProfile.run("pythagoreanTriplet(n)")
 
	# print(len(set([*pythagoreanTriplet(n)])))
		
	# 	print(triplet, triplet[0]**2 + triplet[1]**2 == triplet[2]**2, end="\n\n")

	# res=pythagoreanTriplet(n)
	# import matplotlib.pyplot as plt
	# x=[i for i,_ in res]
	# y=[i for _,i in res]
	# linex=[*range(n)]
	# plt.scatter(x, y, s=0.1, c="k")
	# plt.plot(linex, linex)
	# plt.xlim([0,n])
	# plt.ylim([0,n])
	# plt.gca().set_aspect('equal', adjustable='box')
	# plt.show()
	# pythagorean_triplet(n)

	# for pre in [2.4]:
	# print(pre, pythagoreanTriplet(n, pre)) # 12471 --- 10000
	# 	print(' ')
# 
	# cProfile.run("pythagorean_triplet(n)")
 
	
	# print(' ')
 
	# for a,b,c in pythagorean_triplet(n):
	# 	print(a,b,c)
	pass


# n=sqrt(10**8)

# print(n-sqrt(2*n-1), n/(2+sqrt(2)))
# temp=sqrt(2*n -1)
# H = sum((sqrt(i) for i in range(1, int(n-temp))))
# # n2 = n*n
# # n1_5 = (2*temp -3) * n
# # n1 = temp -1
# # print(math.log(int((H+n1_5+n1)/sqrt(2)), 10))

# print(math.log(H, 10))
