# Perfect Squares
import math
"""
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""

def numSquares(n):
    
    # create square num list
    square_nums = [i**2 for i in range(0, int(math.sqrt(n))+1)]
    
    dp = [float('inf')] * (n+1)

    dp[0] = 0

    for i in range(1, n+1):
        for square in square_nums:
            if i < square:
                break
            
            # dp[index] 0 1 2 3 4 5
            # index     0 1 2 3 1 2
            # dp[4] = min(dp[4], dp[4-4] + 1) = 1
            # dp[5] = min(dp[5], dp[5-4] + 1) = 2
            dp[i] = min(dp[i], dp[i-square] + 1)
    
    return dp[-1]

print(numSquares(12))
