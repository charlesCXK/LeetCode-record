class Solution:
    def removePalindromeSub(self, s: str) -> int:
        oper = 0
        if len(s) == 0:
            return 0
        elif s[::-1] == s:
            return 1
        else:
            return 2
        