#Longest Substring Without Repeating Characters
"""
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""
def lengthOfLongestSubstring(s):
    # 滑动窗口
    left, right = 0, 0
    res = 0
    window = list()
    l = len(s)

    while (right < l) :
        c1 = s[right]
        window.append(c1)

        res = max(res, len(window))
        right += 1

        # window 重复 移动left
        while right < l and s[right] in window :
            c2 = s[left]
            window.remove(c2)
            left += 1

    return res;

print(lengthOfLongestSubstring("abcdabcbb"))
print(lengthOfLongestSubstring("acv"))
print(lengthOfLongestSubstring("a"))

