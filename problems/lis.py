def lisArray(arr, n):
    dp = [[arr[0]]]
    
    for i in range(1, n):
        temp = 0
        tempSubArray = []
        
        for j in range(i):
            if arr[i]>arr[j]:
                if temp<len(dp[j]):
                    tempSubArray = dp[j] 
                    temp = len(dp[j])
     
        dp.append(tempSubArray+[arr[i]])
    
    return max(dp, key=lambda x: len(x))         


def lis(arr, n):
    dp=[1]*n

    for i in range(1, n):
        temp = 0
        
        for j in range(i):
            if dp[j]>=dp[i] and arr[i]>arr[j]:
                temp = max(dp[j], temp)
        dp[i]+=temp
    return max(dp)

if __name__ == "__main__":
    # l = [3,2,6,4,5,1]
    l = [10 , 22 , 9 , 33 , 21 , 50 , 41 , 60]
    # print(lis(l, len(l)))
    print(lisArray(l, len(l)))