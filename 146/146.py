'''
Runtime: 2124 ms, faster than 5.04% of Python3 online submissions 
'''

class LRUCache:

    def __init__(self, capacity: int):
        self.nowTime = 0
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            # has accessed this element recently
            self.cache[key][1] = self.nowTime
            self.nowTime += 1
            return self.cache[key][0]
        return -1

    def put(self, key: int, value: int) -> None:
        self.cache[key] = [value, self.nowTime]
        self.nowTime += 1
        
        if len(self.cache) > self.capacity:
            d = sorted(self.cache.items(), key=lambda d:d[1][1], reverse=False)
            self.cache.pop(d[0][0])


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)