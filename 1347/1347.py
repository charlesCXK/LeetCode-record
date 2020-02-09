class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s = sorted(list(s))
        t = sorted(list(t))
        
        left, right = 0, 0
        same = 0
        
        while left<len(s) and right<len(s):
            if s[left] == t[right]:
                same += 1
                left += 1
                right += 1
            elif ord(s[left]) < ord(t[right]):
                left += 1
            else:
                right += 1
        return len(s)-same