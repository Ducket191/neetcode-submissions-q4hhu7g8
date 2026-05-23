class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        preMap = {i: [] for i in range(numCourses)}
        for src, dst in prerequisites:
            preMap[src].append(dst)
        
        visit = set()
        def dfs(node):
            if node in visit:
                return False
            if preMap[node] == []:
                return True
            
            visit.add(node)
            for child in preMap[node]:
                if not dfs(child):
                    return False
            visit.remove(node)
            preMap[node] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True