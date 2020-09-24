# Letter Combinations of a Phone Number
"""
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

def letterCombinations(digits):
    # 2 - abc
    # 3 - def
    d = {
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz"
    }
    if len(digits) == 0:
        return []
    elif len(digits) == 1:
        return d[int(digits)]
    else:    
        tmp = []
        point = 1
        fst = d[int(digits[0])]
        while point < len(digits):
            sec = d[int(digits[point])]
            for i in fst:
                for j in sec:
                    comb = i + j
                    tmp.append(comb)
            point += 1
            fst = tmp
            tmp = []
        return fst

print(letterCombinations('234'))

