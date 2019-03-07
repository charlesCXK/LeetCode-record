'''
Runtime: 116 ms, faster than 62.50% of Python3

B,C两组的均值都是 sum(A)/len(A). 假设B组长度更短(因为总有一组长度小于 n//2)，为k。
则 sum(B)=sum(A)/len(A)*k,且sum(B)为整数。这就要求sum(A)/len(A)%k==0。从1~n//2枚举每个k的可能值，
'''

class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        n = len(A)
        
        '''
        A: number list
        target: target sum
        ind: now index
        k: k numbers
        visit: To judge whether this state has been visited. Without it I will get a TLE.
        如果当前状态已访问过，且记录的下标 vis_ind 比当前下标 ind 大，则不用管。因为比 ind 下标大且拥有这个状态的情况已经判断过，
        而当前下标 ind 返回True还是False与 下标vis_ind且拥有该状态时的返回值相同，
        都要返回给拥有此状态的最小下标(是这个下标通过递归调用引出后面的步骤)
        '''
        def find(A, target, ind, k, visit):
            if ((target,k) in visit and visit[(target,k)]>ind) or (target<=0 and k>0) or len(A)-ind < k:
                return False
            
            visit[(target, k)] = ind

            if k==0:
                if target == 0:
                    return True
                else:
                    return False
            
            return find(A, target-A[ind], ind+1, k-1, visit) or find(A, target, ind+1, k, visit)
        
        sumA = sum(A)
        for k in range(1, n//2+1):
            if abs(int(sumA/n*k)-sumA/n*k)<=0.0001 and find(A, int(sumA/n*k), 0, k, {}):
                return True
        return False
    