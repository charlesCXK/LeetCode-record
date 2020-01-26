class Solution:
    
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        nTask = len(jobDifficulty)
        memory = {}
        
        def dfs(i, leftd):
            if leftd == 1:
                return max(jobDifficulty[i:])
            
            if (i, leftd) in memory:
                return memory[(i, leftd)]
            
            maxDiff = 0
            ret = math.inf
            for j in range(i, nTask-leftd+1):
                maxDiff = max(maxDiff, jobDifficulty[j])
                ret = min(ret, maxDiff+dfs(j+1, leftd-1))
            
            memory[(i, leftd)] = ret
            return ret
        
        if nTask < d:
            return -1
        return dfs(0, d)