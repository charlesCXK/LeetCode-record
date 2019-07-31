class Solution:
    def longestPalindrome(self, s: str) -> str:
        lens = len(s)
        max_len = 0
        res = ''
        
        for i in range(lens):
            # odd
            left, right, odd_len = i-1, i+1, 1
            odd_str = s[i]
            while left>=0 and right<lens and s[left]==s[right]:
                odd_len += 2
                odd_str = s[left:right+1]
                left -= 1
                right += 1
            # even
            left, right, even_len = i, i+1, 0
            even_str = ''
            while left>=0 and right<lens and s[left]==s[right]:
                even_len += 2
                even_str = s[left:right+1]
                left -= 1
                right += 1
                
            if odd_len >= max_len:
                res = odd_str
                max_len = odd_len
            if even_len >= max_len:
                res = even_str
                max_len = even_len
                
        return res