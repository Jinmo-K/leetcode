import heapq

class Solution:
  def kClosest_quickselect(self, points, K):
    """
    Use quickselect to sort first K elements
    """

    distances = [(self.distToOrigin(point), point) for point in points]

    def partition(left, right):
      pivot = distances[right][0]
      pIndex = left

      for i in range(left, right):
        if distances[i][0] <= pivot:
          distances[pIndex], distances[i] = distances[i], distances[pIndex]
          pIndex += 1
      distances[right], distances[pIndex] = distances[pIndex], distances[right]
      return pIndex

    def select(left, right):
      if left >= right:
        return

      pIndex = partition(left, right)
      if pIndex == K:
        return
      elif pIndex < K:
        select(pIndex + 1, right)
      else:
        select(left, pIndex - 1)

    select(0, len(points) - 1)
    return [closest[1] for closest in distances[:K]]


  def kClosest_pq(self, points, K):
    """
    Using a max-heap, keep adding and popping based on distance.
    In the end, will be left with K smallest distances/points.
    """
    distances = []
    
    for point in points:
      dist = -self.distToOrigin(point)
      # Store in the heap as tuple of (-distance, [x, y])
      heapq.heappush(distances, (dist, point))
      if len(distances) > K:
        heapq.heappop(distances)
    # Retrieve the list of K-smallest points from the tuples
    return [closest[1] for closest in distances]


  def kClosest_sort(self, points, K):
    """
    Sort by Euclidean distance and return the first K elements
    """
    distances = sorted(points, key=lambda point: self.distToOrigin(point))
    return distances[:K]

  
  def distToOrigin(self, point):
    return (point[0]**2 + point[1]**2)**0.5
    
