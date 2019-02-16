class Solution:
    '''
    dp[i][j] means the first i characters of s1 and the first j characters of s2 can be combined to be s3.
    to handle the issue of index, I add '0' to each string, making that the index begins at 1 instead of 0.
    
    Simple derivation:
    if dp[i-1][j]==1 and s1[i]==s3[i+j], dp[i][j] = 1;
    if dp[i][j-1]==1 and s2[j]==s3[i+j], dp[i][j] = 1;
    else,m dp[i][j] = 0;
    '''
    def isInterleave(self, s1: 'str', s2: 'str', s3: 'str') -> 'bool':
        s1, s2, s3 = '0'+s1, '0'+s2, '0'+s3
        len1, len2, len3 = len(s1), len(s2), len(s3)
        dp = [[0 for i in range(len2)] for j in range(len1)]
        
        if len1+len2 != len3+1:
            return False
        # handle the empty string such as s1="", s2="", s3=""
        if len1 == 1:
            return s3 == s2
        if len2 == 1:
            return s3 == s1
        
        # initialize the dp array
        for i in range(1, len1):
            if s1[0:i+1] == s3[0:i+1]:
                dp[i][0] = 1
        for i in range(1, len2):
            if s2[0:i+1] == s3[0:i+1]:
                dp[0][i] = 1
        
        for i in range(1, len1):
            for j in range(1, len2):
                if dp[i-1][j] == 1 and s1[i] == s3[i+j]:
                    dp[i][j] = 1
                if dp[i][j-1] == 1 and s2[j] == s3[i+j]:
                    dp[i][j] = 1

        if dp[len1-1][len2-1] == 1:
            return True
        return False
        
        