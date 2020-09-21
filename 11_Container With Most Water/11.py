# Container With Most Water
"""
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""

def maxArea(height):
    ans = 0
    left = 0
    right = len(height) - 1
    while left < right:
        # 水量取短边，宽度取right-left
        ans = max(ans, min(height[left], height[right])*(right-left))
        # 保留长的，移动短的找下一个可能更长的
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return ans