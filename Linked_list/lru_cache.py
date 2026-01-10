from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value

        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)


lRUCache = LRUCache(2)
lRUCache.put(1, 10);  
lRUCache.get(1);      
lRUCache.put(2, 20);  
lRUCache.put(3, 30);  
lRUCache.get(2);       
lRUCache.get(1);      