class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        target = -1
        for i, ele in enumerate(A):
            if K and ele < 0:
                A[i] = -A[i]
                target = i
                K -= 1
            else:
                break
              
        K = K % 2
        if K > 0:       # 最后翻转一个正数
            if target+1<len(A) and A[target]>A[target+1]:
                A[target+1] = -A[target+1]
            else:
                A[target] = -A[target]
                
        return sum(A)