class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = [[] for i in range(numCourses)]

        # Populate prereqs graph
        for course, pre in prerequisites:
            prereqs[course].append(pre)
        
        # declare seen as safe
        safe = set()
        # current path
        path = set()
        order = []

        def dfs(course):
            # Check 
            if course in path:
                return False
            if course in safe:
                return True
            
            # Mark
            path.add(course)

            # Explore 
            for pre in prereqs[course]:
                if not dfs(pre):
                    return False
            
            path.remove(course)
            safe.add(course)
            order.append(course)

            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return order  

        
