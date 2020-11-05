# Word Break
"""
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""
def wordBreak(s, wordDict):
    n = len(s)
    dp = [False]*(n+1)
    dp[0] = True
    
    # for all segmented s[i:j]
    for i in range(n):
        for j in range(i+1, n+1):
            if (dp[i] and s[i:j] in wordDict):
                dp[j] = True
    return dp[-1]