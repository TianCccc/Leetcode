# Reverse Integer
"""
Input: 123
Output: 321
"""
def reverse(x):
    s = str(x)
    if s[0] == "-":
        x = int("-" + s[1:][::-1])
    else:
        x = int(s[::-1])
    return x if -2147483648< x <2147483647 else 0

print(reverse(123))
print(reverse(1230))
print(reverse(-123))
print(reverse(-1230))
