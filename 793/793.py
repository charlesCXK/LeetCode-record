'''
Runtime: 40 ms, faster than 36.36% of Python3 online submissions
'''
class Solution:
    def preimageSizeFZF(self, K: int) -> int:

        # To count how many zeros in the end of f(num)
        def count(num):
            cnt = 0
            while num:
                cnt += num // 5
                num //= 5
            return cnt 
        
        # Binary search
        l, r = 0, 2**63-1
        while l < r:
            mid = (l+r)//2
            midCount = count(mid)
            
            if midCount < K:
                l = mid + 1
            elif midCount > K:
                r = mid - 1
            else:
                return 5
        return 0
                
        