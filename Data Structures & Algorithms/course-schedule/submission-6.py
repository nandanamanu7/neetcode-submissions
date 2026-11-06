class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = [[] for i in range(numCourses)]

        # Populate prereqs graph
        for course, pre in prerequisites:
            prereqs[course].append(pre)
        
        # declare seen as safe
        safe = set()
        # current path
        path = set()

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

            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True 

        


            
            
            



        