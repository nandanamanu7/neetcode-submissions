import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Shortest path algorithm (Minimum time) when each edge has a different non-negative cost 

        # Populate graph
        graph = [[] for i in range(n+1)]

        for source, target, time in times:
            graph[source].append((target, time))
        
        # Shortest path dijkstras
        minHeap = [(0, k)] # total time, node

        visited = set()
        maxTime = 0

        while minHeap:
            time, node = heapq.heappop(minHeap)

            # Check
            if node in visited:
                continue
            
            # Mark
            visited.add(node)
            maxTime = time

            # Explore neighbors
            for neighbor, edgeTime in graph[node]:
                newTime = time+edgeTime
                # Push new total costs 
                heapq.heappush(minHeap, (newTime, neighbor))

        if len(visited) == n:  
            return maxTime
        
        return -1
        

