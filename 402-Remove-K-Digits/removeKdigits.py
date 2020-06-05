class Solution:
  def removeKdigits(self, num, k):
    res = []
    
    for digit in num:
      # Delete up to k seen digits if they are greater than the current digit
      while k and res and digit < res[-1]:
        res.pop()
        k -= 1
      res.append(digit)
      
    # If remaining k is still > 0, remove the last k digits
    if k:
      res = res[:-k]
    
    return ''.join(res).lstrip('0') or '0'