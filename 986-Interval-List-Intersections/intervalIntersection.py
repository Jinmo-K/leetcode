class Solution:
  def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    A_ptr = 0
    B_ptr = 0
    intersection = []
    
    # Merge the lists
    while A_ptr < len(A) and B_ptr < len(B):
      A_start, A_end = A[A_ptr]
      B_start, B_end = B[B_ptr]

      # Check if the intervals intersect
      start = max(A_start, B_start)
      end = min(A_end, B_end)
      
      if start <= end:
        intersection.append([start, end])
          
      # Keep checking with the interval that has later end time
      if A_end > B_end:
        B_ptr += 1
      else:
        A_ptr += 1
      
    return intersection
    