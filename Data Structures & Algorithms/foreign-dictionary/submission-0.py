class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        topSort =  []
        visit = {}
        def check(a, b):
            m = min(len(a), len(b))
            for i in range(m):
                if a[i] != b[i]:
                    adj[a[i]].add(b[i])
                    return True
            if len(a) > len(b):
                return False
            return True
        

        for i in range(len(words) - 1):
            if not check(words[i], words[i + 1]):
                return ""
        
        for c in adj.keys():
            if not self.dfs(c, adj, visit, topSort):
                return ""
        return "".join(topSort[::-1])
    
    def dfs(self, src, adj, visit, topSort):
        if src in visit:
            return visit[src]
        visit[src] = False

        for neighbor in adj[src]:
            if not self.dfs(neighbor, adj, visit, topSort):
                return False
        visit[src] = True
        topSort.append(src)
        return True