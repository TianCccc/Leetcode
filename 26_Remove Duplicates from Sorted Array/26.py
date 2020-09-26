# Remove Duplicates from Sorted Array
"""
Given nums = [1, 1, 2]
return length = 2
"""

def removeDuplicates(nums):
    ans = 0
    for i in range(len(nums)):
        if nums[ans] != nums[i]:
            ans += 1
            nums[ans] = nums[i]
    return ans+1

print(removeDuplicates([0, 0, 0, 1]))