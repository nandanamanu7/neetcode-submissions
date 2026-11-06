class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = [[] for i in range(numCourses)]

        for course, pre in prerequisites:
            prereqs[course].append(pre)
        
        # if there is a cycle in the graph (2 courses require each other as prereqs, then it is imposisble to finish all courses)

        # safe set, keeps track of safe courses whose prereqs have already been dove into
        safe = set()
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
            
            safe.add(course)
            path.remove(course)

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True

            
            
            



        