class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.child:
                cur.child[c] = TrieNode()
            cur = cur.child[c]
        cur.end = True

    def search(self, word: str) -> bool:
        def dfs(idx, root):
            cur = root
            for i in range(idx, len(word)):
                c = word[i]
                if c == '.':
                    for item in cur.child:
                        if dfs(i + 1, cur.child[item]):
                            return True
                    return False
                elif c not in cur.child:
                    return False
                else:
                    cur = cur.child[c]
            return cur.end
        return dfs(0, self.root)
        