class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        def isPaliindrome(s):
            return s[::-1]==s
        
        lenS = len(palindrome)
        for i in range(lenS//2):
            # print(i, ord(palindrome[i]), ord('a'))
            if ord(palindrome[i]) > ord('a'):
                return palindrome[:i] + 'a' + palindrome[i+1:]
        
        if lenS == 1:
            return ""
        else:
            return palindrome[:lenS-1] + 'b'