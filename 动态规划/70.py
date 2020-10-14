# Climbing Stairs
"""
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

# Solution1
# 暴力算法，第n次的可能性为n-1和n-2的可能性之和
# 超时：看递归树可以知道比如前面的数计算过多次，O(n^2)
# 自顶向下
def climb_stairs_brute(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return climb_stairs_brute(n-1)+ climb_stairs_brute(n-2)

# Solution2
# dp数组迭代
# 简单讲，把之前计算得到的结果储存起来
# 自底向上
def climb_stairs_dp(n):
    dp = {}
    dp[1], dp[2] = 1, 2
    for i in range(3, n+1):
        dp[i] = dp[i-2] + dp[i-1]
    return dp[n]

# Solution2 plus
# 优化空间，只需要dp[1]和dp[2]
def climb_stairs_dp_plus(n):
    one = 1;
    two = 2;
    ans = 0;
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        for i in range(3, n+1):
            ans = one + two
            one = two
            two = ans
        return ans
