'''
Runtime: 96 ms, faster than 74.23% of Python3 online submissions
'''

class Solution:
    # a -> b
    def judgeRequest(self, a, b):
        if b <= 0.5*a+7 or b > a or (b>100 and a<100):
            return False
        return True
        
    def numFriendRequests(self, ages: 'List[int]') -> 'int':
        agelst = [0 for i in range(130)]
        requests = 0
        for age in ages:
            agelst[age] += 1
        
        for i in range(len(agelst)):
            if agelst[i] == 0:
                continue
            # make friends with someone who is as old as him
            if self.judgeRequest(i, i):
                requests += agelst[i] * (agelst[i]-1)

            for j in range(i):
                if agelst[j] and self.judgeRequest(i, j):
                    # print(i, j, agelst[i] * agelst[j])
                    requests += agelst[i] * agelst[j]
        return requests