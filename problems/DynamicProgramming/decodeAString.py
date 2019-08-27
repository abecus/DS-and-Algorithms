
from collections import defaultdict

def waysToDecode(s):
    """
    itype: str of numbers
    rtype: int
    """
    dp = [1 for _ in range(len(s))]
    
    for i in range(1, len(s)):
        if s[i] == '0':
            if s[i-1] == '0' or int(s[i-1])>2:
                return 0
            else:
                dp[i] = dp[i-1] - 1
        else:
            if int(s[i-1:i+1]) <= 26 and s[i-1]!='0':
                dp[i] = dp[i-1]+1
            else:
                dp[i] = max(dp[i-1], dp[i])
            
    return dp[-1], dp
                
        
if __name__ == "__main__":
    print(waysToDecode('151621'))
        