# Minimum Path Sum
"""
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

def minPathSum(grid):
    m = len(grid[0])
    n = len(grid)

    # initialize
    dp = [[0 for i in range(m)] for j in range(n)]

    dp[0][0] = grid[0][0]

    for i in range(1, m):
        dp[0][i] = dp[0][i-1] + grid[0][i]
    
    for j in range(1, n):
        dp[j][0] = dp[j-1][0] + grid[j][0]

    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = min(dp[i-1][j] + grid[i][j], dp[i][j-1] + grid[i][j])
    
    return dp[-1][-1]