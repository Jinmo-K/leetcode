class Solution:
  def findCelebrity(self, n: int) -> int:
    if n <= 1:
      return n - 1
    
    candidate = 0
    
    for i in range(1, n):
      if knows(candidate, i):
        candidate = i
        
    return candidate if self.isCelebrity(candidate, n) else -1
  
  def isCelebrity(self, candidate, n):
    for i in range(n):
      if (knows(candidate, i) or not knows(i, candidate)) and i != candidate:
        return False
    return True