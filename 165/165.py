class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def mask(s):
            sp = s.split('.')
            res, multi = 0, 10000
            for ele in sp:
                n = int(ele)
                res += (n*multi)
                multi /= 10
            return res
        mask1 = mask(version1)
        mask2 = mask(version2)
        
        if mask1 == mask2:
            return 0
        elif mask1 > mask2:
            return 1
        else:
            return -1