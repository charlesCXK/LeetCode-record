class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        sp = s.split()
        return ' '.join(sp[::-1])