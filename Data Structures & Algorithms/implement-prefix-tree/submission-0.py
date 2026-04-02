class PrefixTree:

    def __init__(self):
        self.child = []
        self.val = ""

    def insert(self, word: str) -> None:
        self.child.append(word)

    def search(self, word: str) -> bool:
        if word in self.child:
            return True
        else: return False

    def startsWith(self, prefix: str) -> bool:
        for item in self.child:
            if prefix in item:
                return True
        return False
        
        