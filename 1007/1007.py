class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        def tryswap(A, B):
            visit = []
            n = len(A)
            minSwapNum = 99999
            for i,ele in enumerate(A):
                if ele in visit:
                    continue
                visit.append(ele)       # 把这个当做最后交换完之后的元素
                swapNum = 0
                for j in range(n):
                    if A[j] == ele:
                        continue
                    elif B[j] == ele:
                        swapNum += 1
                    else:
                        swapNum = 99999
                        break
                minSwapNum = min(minSwapNum, swapNum)
            return minSwapNum
        
        swapNum = min(tryswap(A, B), tryswap(B, A))
        if swapNum == 99999:
            return -1
        return swapNum