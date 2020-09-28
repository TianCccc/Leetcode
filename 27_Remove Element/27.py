# Remove Element
"""
Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.
"""

def removeElement(nums, val):
    for i in range(len(nums)-1, -1, -1):
        if nums[i] == val:
            nums.pop(i)
    return len(nums)

print(removeElement([3, 2, 2, 3], 3))