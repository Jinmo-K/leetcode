class Solution:
  def islandPerimeter(self, grid: List[List[int]]) -> int:
    perimeter = 0

    for r in range(len(grid)):
      for c in range(len(grid[0])):
        if grid[r][c] == 1:
          perimeter += 4
          # check top neighbour
          if r > 0 and grid[r-1][c] == 1:
            perimeter -= 2
          # check left neighbour
          if c > 0 and grid[r][c-1] == 1:
            perimeter -= 2
            
    return perimeter
