class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]

        # Graph of courses and all their required prereqs 
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        path = set()
        safe = set()

        def dfs(course):

            # Check
            if course in path:
                return False
            
            if course in safe:
                return True
            
            # Mark
            path.add(course)

            # Explore
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            
            # Mark
            path.remove(course)
            safe.add(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True







            
        