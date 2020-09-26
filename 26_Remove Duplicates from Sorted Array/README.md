# Note
 _s1_ 
```diff
! `in place`
ans = 0
    for i in range(len(nums)):
        if nums[ans] != nums[i]:
            ans += 1
            nums[ans] = nums[i]
    return ans+1
```
