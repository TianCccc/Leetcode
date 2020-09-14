#Longest Palindromic Substring
"""
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
"""
def longestPalindrome(s):
    # From center
    if len(s) == 0:
        return ""
    else:
        temp = s[0]
        for i, c in enumerate(s):
            l = i
            r = i

            # center == 1
            while ( l-1 >=0 and r+1 <len(s) and s[l-1] == s[r+1]) :
                l -= 1
                r += 1
                # length = r-l+1
                substring = s[l:r+1]
                if len(substring) >= len(temp):
                    temp = substring
            
            l = i
            r = i
            # center == 2
            while ( l >=0 and r+1 <len(s) and s[l] == s[r+1]):
                
                # length = r-l
                r += 1
                substring = s[l:r+1]
                l -= 1
                if len(substring) >= len(temp):
                    temp = substring

        return temp
    
    

print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))
print(longestPalindrome("cbbcd"))
print(longestPalindrome("a"))
print(longestPalindrome("bacab"))
print(longestPalindrome("cbbbd"))
print(longestPalindrome(""))
print(longestPalindrome("aaabaaaa"))
print(longestPalindrome("cccc"))


