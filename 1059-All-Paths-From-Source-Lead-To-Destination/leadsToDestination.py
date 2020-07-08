class Solution:
    def leadsToDestination(self, n, edges, source, destination):
        path = set()
        graph = {}
        
        # Create the graph
        for s, t in edges:
            graph[s] = graph.get(s, []) + [t]
            
        # Destination has outgoing edges
        if destination in graph:
            return False
        
        def dfs(node):
            if node == destination:
                return True
            # Node != destination and has no outgoing edges
            if node not in graph:
                return False
            # Add the node to the current path for cycle detection
            path.add(node)
            
            for neighbour in graph[node]:
                # Neighbour is part of cycle or has no path to destination
                if neighbour in path or not dfs(neighbour):
                    return False
                
            path.remove(node)
            return True
                
        return dfs(source)