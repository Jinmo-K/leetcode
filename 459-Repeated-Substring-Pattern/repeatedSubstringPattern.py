class Solution:
  def repeatedSubstringPattern(self, s):
    fail_table = [0] * len(s)
    left = 0

    for right in range(1, len(s)):
      while s[left] != s[right] and left > 0:
        left = fail_table[left-1]
      if s[left] == s[right]:
        left += 1
        fail_table[right] = left
    
    length_repeated = fail_table[-1]
    length_substring = len(s) - length_repeated

    return length_repeated != 0 and length_repeated % length_substring == 0
