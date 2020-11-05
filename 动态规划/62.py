# Unique Paths
"""
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
"""

def uniquePaths(m, n):
    # initialize
    dp = [[1 for i in range(m)] for j in range(n)]

    dp[0][0] = 0
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    dp[0][0] = 1
    
    return dp[n-1][m-1]