class Solution:
  def heightChecker(self, heights: List[int]) -> int:
    min_height = float('inf')
    max_height = -float('inf')
    counts = {}
    num_moves = 0
    # Find min, max, and counts of heights
    for height in heights:
      counts[height] = counts.get(height, 0) + 1
      min_height = min(min_height, height)
      max_height = max(max_height, height)
    
    ptr = 0
    # count number of positions where a height is not 
    # in its correct position
    for height in range(min_height, max_height + 1):
      if height in counts:
        for _ in range(counts[height]):
          if heights[ptr] != height:
            num_moves += 1
          ptr += 1
    
    return num_moves