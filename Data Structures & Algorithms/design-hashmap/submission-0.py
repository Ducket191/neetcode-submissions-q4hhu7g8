class MyHashMap:

    def __init__(self):
        self.data = []

    def put(self, key: int, value: int) -> None:
        for item in self.data:
            if item[0] == key:
                item[1] = value
                return None
        l = [key, value]
        self.data.append(l)

    def get(self, key: int) -> int:
        for item in self.data:
            if item[0] == key:
                return item[1]
        return -1

    def remove(self, key: int) -> None:
        for item in self.data:
            if item[0] == key:
                self.data.remove(item)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)