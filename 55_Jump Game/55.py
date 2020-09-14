# Jump Game
"""
Input: nums = [2,3,1,1,4]
Output: True
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
"""
def canJump(nums):
    # Greedy
    farthest = 0
    for i, jump in enumerate(nums):
        if farthest >= i and i+jump > farthest: # 当前位置能到达 and 下一跳超过farthest
            farthest = i + jump
    return farthest >= i