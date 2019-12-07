class Solution:
    ans = []

    '''
    s: the current string.
    step: the step-th position.
    n: total positions.
    k: delta of every two consecutive digits. 
    '''
    def dfs(self, s, step, n, k):
        # print(s, step, n, k)
        if step==n:
            self.ans.append(int(s))
            return
        
        if step == 0:
            if n == 1:
                self.dfs('0', step+1, n, k)
            for i in range(1, 10):      # prevent the leading '0'
                self.dfs(str(i), step+1, n, k)
        else:
            lastone = ord(s[-1]) - ord('0')     # convert str to number
            flag = 0
            if lastone+k>=0 and lastone+k<=9:
                flag = 1
                self.dfs(s+str(lastone+k), step+1, n, k)
            if lastone-k>=0 and lastone-k<=9 and k!=0:
                flag = 1
                self.dfs(s+str(lastone-k), step+1, n, k)  
            if flag == 0:
                return
            
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        self.ans = []
        self.dfs('', 0, N, K)
        return self.ans