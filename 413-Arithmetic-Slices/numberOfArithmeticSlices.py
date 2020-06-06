class Solution:
  def numberOfArithmeticSlices(self, A: List[int]) -> int: 
    num_slices = 0
    add = 0
    
    for i in range(2, len(A)):
      if (A[i] - A[i-1]) == (A[i-1] - A[i-2]):
        add += 1
        num_slices += add
      else:
        add = 0
    return num_slices