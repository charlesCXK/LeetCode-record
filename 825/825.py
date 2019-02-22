'''
3572 ms
Sort the ages, because each one only needs to consider someone who is not older than him.
'''

class Solution:
    # a -> b
    def judgeRequest(self, a, b):
        if b <= 0.5*a+7 or b > a or b>100 and a<100:
            return False
        return True
    
    def numFriendRequests(self, ages: 'List[int]') -> 'int':
        ages.sort(reverse=True)
        requestnum = 0
        
        it1, it2 = 0, 0
        while it1 < len(ages):
            it2 = it1 + 1
            request = 0
            while it2 < len(ages):
                if self.judgeRequest(ages[it1], ages[it2]):
                    request += 1
                it2 += 1
            requestnum += request
            it1 += 1
            # skip the same element
            while it1<len(ages) and ages[it1] == ages[it1-1]:
                requestnum += request
                it1 += 1
        return requestnum