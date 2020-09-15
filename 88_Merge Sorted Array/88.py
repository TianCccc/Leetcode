# Merge Sorted Array
"""
Input: nums1=[1,2,3,0,0,0], m=3
       nums2=[2,5,6],       n=3
Output:[1,2,2,3,5,6]
"""
def merge(nums1, m, nums2, n):
    
    while m > 0 and n > 0:
        if nums1[m-1] < nums2[n-1]:
            nums1[m-1+n] = nums2[n-1]
            n = n - 1
        else:
            nums1[m-1+n], nums1[m-1] = nums1[m-1], nums1[m-1+n]
            m = m - 1
    if m == 0 and n > 0:
        nums1[:n] = nums2[:n]
