class Solution:
    def convertToTitle(self, n: int) -> str:
        if n == 0:
            return ''
        m = ['Z']+[chr(i+ord('A')) for i in range(25)]
        
        # the last position
        tmp = n % 26
        n = n-tmp if tmp>0 else n-26
        
        num26 = n//26   # how many 26 are there
        return self.convertToTitle(num26) + m[tmp]