class Solution:
    '''
    [9,3,5]: maximum is 9, thus the former array is [1,3,5] ==>
    [1,3,5]: maximum is 5, thus the former array is [1,3,1] ==>
    [1,3,1]: maximum is 3, thus the former array is [1,1,1] ==> True
    '''
    def isPossible(self, target: List[int]) -> bool:
        def findMaxIndex(l):
            maxNum, maxIdx = -1, -1
            for i,e in enumerate(l):
                if e > maxNum:
                    maxNum = e
                    maxIdx = i
            return maxNum,maxIdx
        
        target = target.copy()
        nowSum = sum(target)
        maxNum, maxIdx = findMaxIndex(target)
        
        while maxNum>(nowSum-maxNum) or maxNum==1:
            # print(maxNum, maxIdx, nowSum, target)
            if maxNum == 1:
                return True
            toReplace = maxNum - (nowSum - maxNum)
            nowSum = nowSum - maxNum + toReplace
            target[maxIdx] = toReplace
            
            # print(target)
            maxNum, maxIdx = findMaxIndex(target)
            
        return False