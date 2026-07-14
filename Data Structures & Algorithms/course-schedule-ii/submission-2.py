class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        path = set()
        visit = set()
        res = []

        def dfs(crs):
            if crs in path:
                return False
            if crs in visit:
                return True

            path.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            path.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res