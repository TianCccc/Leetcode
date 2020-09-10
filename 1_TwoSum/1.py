#Two Sum
"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
"""
def twoSum_1(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    n = len(nums)
    for i in range(n):
        a = target - nums[i]
        if a in nums:
            j = nums.index(a)
            if i != j:
                return [i, j]

print(twoSum_1([2,7,11,15], 9))

def twoSum_2(nums, target):
    """
    hash map
    """
    hashmap = {}
    for i in range(len(nums)):
        if target - nums[i] not in hashmap:
            #字典为空，赋值字典   [2,0],[7,1]...
            hashmap[nums[i]] = i
        else:
            return [hashmap[target - nums[i]], i]

print(twoSum_2([2,7,11,15], 9))