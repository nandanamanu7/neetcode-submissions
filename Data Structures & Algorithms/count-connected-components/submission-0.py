class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
    
        graph = [[] for i in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        components = 0

        visited = set()

        def dfs(node):
            # Check
            if node in visited:
                return False
            
            # Mark 
            visited.add(node)

            # Explore 
            for neighbor in graph[node]:
                dfs(neighbor)

            return True 

        
        for i in range(n):
            if(dfs(i)):
                components += 1
        
        return components


        