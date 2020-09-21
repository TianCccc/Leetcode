# Integer to Roman
"""
Input: 3
Output: "III"

Input: 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""
def intToRoman(num):
    # Rules
    """
    M: 1000
    D: 500
    C: 100      CD: 400     CM: 900
    L: 50
    X: 10       XL: 40      XC: 90
    V: 5
    I: 1        IV: 4       IX: 9
    """
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerals = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

    result = ''

    for i in range(0, len(values)):
        while num >= values[i]:
            num -= values[i]
            result += numerals[i]
    
    return result