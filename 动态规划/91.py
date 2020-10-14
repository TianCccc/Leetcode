# Decode Ways
"""
Input: s = "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Input: s = "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""

# 边界值很关键，dp[0]对应s[0]
# 分情况讨论：最后两位有没有0
#            最后两位超不超过26

def numDecodings(s):
    if not s or s[0] == '0':
        return 0
    if len(s) == 1:
        return 1
    
    dp = {}
    # 一个数肯定是1
    dp[0] = 1
    # 为dp[2]赋值
    if len(s) > 1:
        if s[1] == '0':
            if int(s[0:2]) <= 26:
                dp[1] = 1
            else:
                return 0
        else:
            if int(s[0:2]) <= 26:
                dp[1] = 2
            else:
                dp[1] = 1
    
    for i in range(2, len(s)):
        if s[i] == '0':
            if s[i-1] == '0':
                return 0
            else:
                if int(s[i-1:i+1]) <= 26:
                    dp[i] = dp[i-2]
                else:
                    return 0
        else:
            if s[i-1] == '0':
                dp[i] = dp[i-1]
            else:
                if int(s[i-1:i+1]) <= 26:
                    dp[i] = dp[i-2] + dp[i-1]
                else:
                    dp[i] = dp[i-1]
    return dp[len(s)-1]

print(numDecodings("226"))