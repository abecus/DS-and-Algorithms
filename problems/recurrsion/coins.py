#   number of ways to get a amount given different 
# coin values with inf amount

from functools import lru_cache
@lru_cache(None)
def coins(idx, amt):
	global arr, l
	if amt==0:
		return 1
	res=0
	for i in range(l):
		coin = arr[i]
		if not coin>amt:
			res+=coins(i+1, amt-coin)
	return res

if __name__ == "__main__":
	arr, amt = [5,2,1], 5
	l = len(arr)
	
	print(coins(0, amt))
	print(coins.cache_info())
