class LRUCache:

    def __init__(self, capacity: int):
        self.store = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if not key in self.store:
            return -1
        val = self.store.pop(key)
        self.store[key] = val
        return val
        
    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.store.pop(key)
        elif len(self.store) >= self.capacity:
            first_key = next(iter(self.store))
            self.store.pop(first_key)
        self.store[key] = value