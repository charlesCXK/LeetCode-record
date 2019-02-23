'''
Runtime: 128 ms, faster than 86.22% of Python3 online submissions 
from small to big, the number of 2*x should be no smaller than the number of x. So minus the number of 2*x with the number of x, to see if the number of 2 *x is still not negative.
'''

class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        posit, negat = [], []
        for item in A:
            if item > 0:
                posit.append(item)
            elif item < 0:
                negat.append(abs(item))
        
        def judgeValid(lst):
            length = len(lst)
            if length%2 == 1:
                return False
            if length == 0:
                return True
            
            max_num = max(lst)
            table = [0 for i in range(max_num*2+100)]
            
            for i in range(length):
                table[lst[i]] += 1

            for i in range((max_num*2+100)//2-1):
                if table[i]:
                    table[i*2] -= table[i]
                    if table[i*2] < 0:
                        return False
            return True
        
        return judgeValid(posit) and judgeValid(negat)