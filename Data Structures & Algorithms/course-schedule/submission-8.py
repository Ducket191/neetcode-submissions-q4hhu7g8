class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        adj = {i: [] for i in range(numCourses)}
        res = 0
        for dst, src in prerequisites:
            adj[src].append(dst)
        
        visit = set()
        def dfs(crs):
            if crs in visit:
                return False
            if adj[crs] == []:
                return True
            
            visit.add(crs)
            for item in adj[crs]: #(1)
                if not dfs(item):
                    return False
            visit.remove(crs) 
            adj[crs] = [] #since there're no False in (1), we can consider this crs can be completed
                            # without any prerequisites => []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True