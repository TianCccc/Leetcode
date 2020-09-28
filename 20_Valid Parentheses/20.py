# Valid Parentheses
"""
Input: s = "()"
Output: true

Input: s = "{[]}"
Output: true

Input: s = "([)]"
Output: false
"""

def isValid(s):
    d = {')': '(',
         ']': '[',
         '}': '{'}
    stack = []
    for i in s:
        if (len(stack) != 0) and i in d:
            # stack last element compared with element i
            if stack[-1] == d[i]:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)
    
    return not stack

print(isValid("([)]"))
