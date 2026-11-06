class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n-1:
            return False
        
        # build a graph 

        graph = [[] for i in range(n)]

        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        visited = set()

        def dfs(node):
            
            # Mark
            visited.add(node)

            # Explore 
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        # Only dfs 0, so that it adds every connected node to the visited set
        dfs(0)

        return len(visited) == n

