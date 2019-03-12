class Solution:
    import math
    def clumsy(self, N: int) -> int:
        oper = 0
        ret = N
        N -= 1
        
        while N >= 1:
            if oper == 0:       # *
                ret *= N
                oper = (oper+1)%4
                N -= 1
            elif oper == 1:     # /
                ret = math.floor(ret/N)
                oper = (oper+1)%4
                N -= 1  
            elif oper == 2:     # +
                ret += N
                oper = (oper+1)%4
                N -= 1
            else:       # -
                if N >= 3:
                    ret -= (math.floor(N*(N-1)/(N-2)))
                    N -= 3
                    oper = 2
                elif N == 2:
                    ret -= 2
                    return ret
                elif N == 1:
                    ret -= 1
                    return ret
        return ret
                
                