class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        lenArr = len(arr)
        vis = [0 for i in range(lenArr)]
        maxJumpNum = [0 for i in range(lenArr)]
        
        def dfs(idx):
            if vis[idx] == 1:
                return
            
            vis[idx] = 1
            
            # enumerate all the indices we can reach
            idxList = []
            for i in range(1, d+1):
                if idx-i<0 or arr[idx]<=arr[idx-i]:
                    break
                idxList.append(idx-i)
            for i in range(1, d+1):
                if idx+i>=lenArr or arr[idx]<=arr[idx+i]:
                    break
                idxList.append(idx+i)
            
            # print(idx, idxList)
            
            maxJump = 1
            for index in idxList:
                if vis[index] == 1:
                    maxJump = max(maxJump, maxJumpNum[index]+1)
                else:
                    dfs(index)
                    maxJump = max(maxJump, maxJumpNum[index]+1)
            maxJumpNum[idx] = maxJump
            return
        
        for i in range(lenArr):
            dfs(i)
        # print(maxJumpNum)
        return max(maxJumpNum)