class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        
        # Go through each course, and its corresponding prerequisites
        # Add the courses as values for the prerequisite as key
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        path = set()

        safe = set()


        def dfs(course):
            # Check

            # If course in path, unsafe.
            if course in path:
                return False
            
            # Already checked this branch
            if course in safe:
                return True 
            
            # Mark
            path.add(course)

            # Explore
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            
            path.remove(course)
            safe.add(course)

            return True
        
        # Check every single course
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True 
            

        