class Solution:
  def distributeCandies(self, candies):
    types = set(candies)
    return min(len(candies) // 2, len(types))
