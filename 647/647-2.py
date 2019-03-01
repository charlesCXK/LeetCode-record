'''
Runtime: 116 ms, faster than 88.68% of Python3 online submissions 
每次寻找回文串的中心。假设 s[a ~ b]是回文串，那么s[a+1 ~ b-1]也是回文串。
所以每次枚举回文串的中心，向两边扩散，看最多能扩散到多少。
'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        
        for center in range(2*n):
            left = center // 2  # 0, 0, 1, 1......n-1, n-1
            right = left + (center%2)   # 0, 1, 1, 2......
            
            while left>=0 and right<n and s[left]==s[right]:
                left -= 1
                right += 1
                ans += 1
        return ans