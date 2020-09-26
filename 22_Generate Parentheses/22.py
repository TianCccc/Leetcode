# Generate Parentheses
"""
Input: 3
Output:[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
def generateParenthesis(self, n):
      if n == 0:
        return []
      result = []
      def helper(l, r, item, result):
          if r < l:
              return
          if l == 0 and r == 0:
              result.append(item)
          if l > 0:
              helper(l-1, r, item + '(', result)
          if r > 0:
              helper(l, r-1, item + ')', result)
        
      helper(n, n, '', result)
      
      return result