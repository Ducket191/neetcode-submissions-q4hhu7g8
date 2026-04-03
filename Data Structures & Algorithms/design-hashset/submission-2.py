class MyHashSet:

    def __init__(self):
        self.box = defaultdict(int)

    def add(self, key: int) -> None:
        if self.box[key] == 0:
            self.box[key] = 1

    def remove(self, key: int) -> None:
        self.box[key] = 0
        

    def contains(self, key: int) -> bool:
        if self.box[key] == 0:
            return False
        else:
            return True
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)