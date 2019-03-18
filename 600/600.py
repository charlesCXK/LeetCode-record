'''
Runtime: 48 ms, faster than 73.17% of Python3 online submissions
'''

class Solution:
    def findIntegers(self, num: int) -> int:
        binary = bin(num)[2:]
        n = len(binary)
        res = 0
                
        # dp[i]: 从右数，最后一个出现的1在右数第 i 位的时候，一共有多少种 (位数从1开始计数)
        dp = [0 for i in range(max(3, n+2))]
        dp[0] = 1
        dp[1] = 1
        dp[2] = 1
        
        seqSum = dp[0] + dp[1]
        
        for i in range(3, n+2):
            dp[i] = seqSum
            seqSum += dp[i-1]
        
        # assume the n-th bit is 0.
        # res += dp[n-1]+dp[n-2]....  = res + dp[n+1]
        # res += dp[n+1]
        
        # assume that the n-th bit is 1.
        for i in range(n):
            # 如果是1，把它变成0，然后考虑后面的位有可能是1
            if binary[i] == '1':        # make i to be 0, i+1 to be 1. (n-i-1)-th bit from the right side
                res += (dp[n-i+1])
            # 当前位和前面的都是1，再往后考虑情况就不成立了，直接break
            if i>0 and binary[i]==binary[i-1] and binary[i]=='1':
                break
        
        # 扫一遍自身是否成立
        flag = True
        for i in range(1, n):
            if binary[i]==binary[i-1] and binary[i]=='1':
                flag = False
        if flag:
            res += 1
                            
        return res