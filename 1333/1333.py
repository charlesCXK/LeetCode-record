class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        from functools import cmp_to_key

        def cmp(x,y):
            if x[1] != y[1]:
                return x[1]-y[1]
            else:
                return x[0]-y[0]

        filtered = []
        for item in restaurants:
            if item[2]>=veganFriendly and item[3]<=maxPrice and item[4]<=maxDistance:
                filtered.append((item[0], item[1]))
        
        filtered = sorted(filtered, key=cmp_to_key(cmp), reverse=True)
        
        ret = []
        for item in filtered:
            ret.append(item[0])
        return ret
        