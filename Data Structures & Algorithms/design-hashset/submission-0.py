class MyHashSet:

    def __init__(self):
        self.box = []

    def add(self, key: int) -> None:
        if not key in self.box:
            self.box.append(key)

    def remove(self, key: int) -> None:
        for item in self.box:
            if item == key:
                self.box.remove(item)
        

    def contains(self, key: int) -> bool:
        for item in self.box:
            if item == key:
                return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)