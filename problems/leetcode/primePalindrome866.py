"""
_________________________866. Prime Palindrome_________________________
Difficulty: Medium		Likes: 105		Dislikes: 294		Solution: Available
Total Accepted: 8.9K		Total Submission: 43.3K		Acceptance Rate: 20.4%
Tags:  Math


Find the smallest prime palindrome greater than or equal to N.
Recall that a number is prime if it's only divisors are 1 and itself, and it is greater than 1. 
For example, 2,3,5,7,11 and 13 are primes.
Recall that a number is a palindrome if it reads the same from left to right as it does from right to left. 
For example, 12321 is a palindrome.
 

Example 1:

Input: 6
Output: 7


Example 2:

Input: 8
Output: 11


Example 3:

Input: 13
Output: 101



 
Note:

1 <= N <= 10^8
The answer is guaranteed to exist and be less than 2 * 10^8.

"""

def primePalindrome(N ):
    # primesPlain = []
    
    if N==1:
        N+=1
    i=N
    
    def isPrime(n):
        return all(n%d for d in range(2, int(pow(n, 0.5))+1))
    
    def isPalindrome(x):
        j, i=len(x)-1, 0
        while i<j:
            if x[i]==x[j]:i,j = i+1,j-1
            else:return 0
        return 1
                        
    while 1:
        if isPalindrome(str(i)) and isPrime(i):
            return i
        i+=1
        if 10**7 < i < 10**8:
            i = 10**8
            
    # with open('primsPalindromes.text', 'w') as f:
    #     w = f.write
    #     for i in range(2, N+1):
    #         if isPalindrome(str(i)) and isPrime(i):
    #             t = f'{i},'
    #             w(t)

    #     if 10**7 < i < 10**8:
    #         i = 10**8

if __name__ == "__main__":
    N = 6
    print(primePalindrome(N))


"""
"""
