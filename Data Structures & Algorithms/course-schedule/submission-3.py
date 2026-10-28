class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]

        # For all courses in map of prereqs
        for course, prereq in prerequisites:
            # The graph of prereqs at that specific spot are appended with the course that is the new prereq
            graph[prereq].append(course)

        # Keeps track of the path from the course down to the lowest prereq
        path = set()
        # Keeps track of safe courses which have already verified all prerequisites
        safe = set()

        # Deep-dives each course 
        def dfs(course):
            # Check

            # We check whether the course is in the path so far, since if a prereq to a course is a course that req. a prereq, then cycle detected 
            if course in path:
                return False
            
            # If course already est. safe
            if course in safe:
                return True

            # Mark
            path.add(course)

            # Explore all neighbors until no more left or returns False
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            
            # After all dfs is completed, this value can be removed from the path and marked safe 
            path.remove(course)
            safe.add(course)

            return True
        
        # Go through numbers 0-total numCourses
        for course in range(numCourses):
            # Check down all paths of Course 
            if not dfs(course):
                return False
        
        return True
    





            
        