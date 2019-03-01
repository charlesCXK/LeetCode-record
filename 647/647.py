'''
572 ms
暴力枚举
'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        ret = 0
        
        def judge(s):
            return s == s[::-1]
        
        for i in range(length):
            for j in range(i+1, length+1):
                substr = s[i:j]
                if judge(substr):
                    ret += 1
        return ret
                
        