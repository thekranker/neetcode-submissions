class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = { i: [] for i in range(numCourses) }
        for course, prereq in prerequisites:
            preMap[course].append(prereq)
        

        seen = set()
        def dfs(course: int, seen: set):

            if course in seen:
                return False

            if preMap[course] == []:
                return True
            
            seen.add(course)
            for prereq in preMap[course]:
                if not dfs(prereq, seen):
                    return False
            
            seen.remove(course)
            preMap[course] = []
            return True

        
        for course, prereq in prerequisites:
            if not dfs(course, seen):
                return False
        return True