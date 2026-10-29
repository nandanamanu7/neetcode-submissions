from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        q = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])
        
        minutes = 0

        directions = [[-1,0], [1, 0], [0,1], [0,-1]]

        while(fresh > 0 and q):
            minutes += 1
            lenq = len(q)
            for i in range(lenq):
                position = q.popleft()

                for d in directions:
                    newr = position[0] + d[0]
                    newc = position[1] + d[1]
                    if (newr < rows and newr > -1 and newc > -1 and newc < cols and grid[newr][newc] == 1):
                        grid[newr][newc] = 2
                        q.append([newr, newc])
                        fresh -=1 
            
        if (fresh > 0):
            return -1
        
        return minutes
            


        
        