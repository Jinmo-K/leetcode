import heapq

class Solution:
  def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
    graph = [{} for _ in range(N+1)]
    seen = set()
    queue = [(0, K)]
    max_delay = 0
    
    for source, target, delay in times:
      graph[source][target] = delay
      
    while queue:
      delay, node = heapq.heappop(queue)
      if node not in seen:
        seen.add(node)
        N -= 1
        for neighbour, neigh_delay in graph[node].items():
          if neighbour not in seen:
            heapq.heappush(queue, (delay + neigh_delay, neighbour))
        max_delay = delay
                            
      return max_delay if not N else -1
