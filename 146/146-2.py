'''
Runtime: 140 ms, faster than 52.95% of Python3 online submissions 
'''

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            # has accessed this element recently
            self.cache.move_to_end(key, last=False)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key, last=False)
        
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=True)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)