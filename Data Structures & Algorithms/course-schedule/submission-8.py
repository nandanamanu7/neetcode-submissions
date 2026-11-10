class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = [[] for i in range(numCourses)]

        for course, prereq in prerequisites:
            courses[course].append(prereq)
        
        path = set()
        safe = set() 

        def dfs(course):
            # Check 
            if (course in path):
                return False 
            
            if (course in safe):
                return True
            
            # Mark
            path.add(course)

            # Explore
            for pre in courses[course]:
                if (dfs(pre) == False):
                    return False
            
            # Mark
            path.remove(course)
            safe.add(course)


        for i in range(numCourses):
            if dfs(i) == False:
                return False
            
        return True
            
            