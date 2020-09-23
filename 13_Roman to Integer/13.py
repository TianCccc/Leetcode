# Roman to Integer
"""
Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
"""

def romanToInt(s):
    d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    str_length = len(s)
    ans = 0
    for i in range(str_length):
        if i < len(s) - 1 and d[s[i]] < d[s[i+1]]:
            ans -= d[s[i]]
        else:
            ans += d[s[i]]
    return ans

print(romanToInt("III"))