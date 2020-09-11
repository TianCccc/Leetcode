#Longest Substring Without Repeating Characters
"""
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""
# def lengthOfLongestSubstring(s):
#     # 滑动窗口
#     left, right = 0, 0
#     res = 0
#     window = list()
#     l = len(s)

#     while (right < l) :
#         c1 = s[right]
#         window.append(c1)
#         print(window)
#         right += 1
#         # window 重复
#         # 移动left
#         while right < l and s[right] in window :
#             c2 = s[left]
#             window.remove(c2)
#             left += 1

#         res = max(res, right - left)
#         print(res)

#     return res;
def lengthOfLongestSubstring(s):
    k = -1 # 左指针
    res = 0 # 长度
    window = {} 

    for i, c in enumerate(s):
        # print (i, c)
        # 0, a
        # 1, b
        # 2, c
        if c in window and window[c] > k : # c在窗口中，而且这次的下标大于上次出现的下标
            k =  window[c] # 比如 abb, 起始要变成第二个b，而不是第一个b
            window[c] = i
        else:
            window[c] = i # c不在窗口中，移动右指针，添加元素
            res = max(res, i-k)
    return res

print(lengthOfLongestSubstring("abcabcbb"))
