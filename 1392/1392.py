class Solution:
    def longestPrefix(self, s: str) -> str:
        lens = len(s)
        for l in range(lens-1, 0, -1):
            if s[:l] == s[lens-l:]:
                return s[:l]
        return ""