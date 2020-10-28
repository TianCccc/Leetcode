# Unique Paths II
"""
Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""

def uniquePathsWithObstacles(self, obstacleGrid):
      m = len(obstacleGrid[0])
      n = len(obstacleGrid)
        
      if m == n == 1 and obstacleGrid[0][0] == 0:
          return 1
            
        
      # initialize
      dp = [[0 for i in range(m)] for j in range(n)]

      for i in range(m):
          if obstacleGrid[0][i] == 0:
              dp[0][i] = 1
          else:
              break
      for j in range(n):
          if obstacleGrid[j][0] == 0:
              dp[j][0] = 1
          else:
              break
      
      dp[0][0] = 0

      for i in range(1, n):
          for j in range(1, m):
              if obstacleGrid[i][j] == 1:
                  dp[i][j] = 0
              else:
                  dp[i][j] = dp[i-1][j] + dp[i][j-1]

      return dp[n-1][m-1]