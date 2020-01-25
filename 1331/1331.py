class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sortArr = sorted(arr)
        rankDict = {}
        it = 0
        rank = 1
        while it < len(arr):
            if it>0 and sortArr[it]==sortArr[it-1]:
                pass
            else:
                rankDict[sortArr[it]] = rank
                rank += 1
            it += 1
            
        ret = []
        for item in arr:
            ret.append(rankDict[item])
        return ret