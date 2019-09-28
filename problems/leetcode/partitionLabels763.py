'''
763. Partition Labels

A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

Note:
S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.
'''
def partitionLabels(S):
    h = {c: i for i, c in enumerate(S)}
    
    
    i = 0
    ans = []
    while i<len(S):
        
        ele = S[i]
        temp = h[ele]
        j = i+1
        
        while j < temp+1:
            ele = S[j]
            temp = max(temp, h[ele])   
            j+=1
            
        ans.append(temp)
        i=temp+1
    
    for i in reversed(range(1, len(ans))):
        ans[i] = ans[i]-ans[i-1]
    
    ans[0]+=1
        
    return ans
        
if __name__ == "__main__":
    S = "ababcbacadefegdehijhklij"
    S = "abcaecjkj" #[6, 3]
    # S ='s' #[1]
    # S = "qiejxqfnqceocmy" #[13,1,1]
    print(partitionLabels(S))