# 4Sum
"""
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""

def fourSum(nums, target):

    l = len(nums)
    result = []
    nums.sort()
    # [-2, -1, 0, 0, 1, 2]


    for i in range(l-3):
        if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
            break
        if nums[i] + nums[l-1] + nums[l-2] + nums[l-3] < target:
            continue

        # deal with the same element
        if i > 0 and nums[i] == nums[i-1]:
            continue

        for j in range(i+1, l-2):                   ### j = i+1; range(i+1, l-2)
            if j > i+1 and nums[j] == nums[j-1]:    ### j > i+1; j can't compared with i+1
                continue
            lf = j+1
            rt = l-1

            while lf < rt:
                tmp = nums[i] + nums[j] + nums[lf] + nums[rt]
                if tmp == target:
                    result.append([nums[i], nums[j], nums[lf], nums[rt]])
                    while lf+1 < rt and nums[lf] == nums[lf+1]:
                        lf += 1
                    lf += 1
                    while rt < rt-1 and nums[rt] == nums[rt-1]:
                        rt -= 1
                    rt -= 1
                elif tmp < target:
                    lf += 1
                else:
                    rt -= 1
    return result
