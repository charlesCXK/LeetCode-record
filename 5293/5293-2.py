'''
[description]
Sliding window.
'''
class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):

        begin, end = 0, 0
        curr = collections.defaultdict(int)     # record the number of different characters
        res = collections.defaultdict(int)      # record the number of occurrences 
        while end < len(s):
            curr[s[end]] += 1
            end += 1

            while minSize <= (end - begin) <= maxSize:
                if len(curr) <= maxLetters:
                    res[s[begin:end]] += 1
                    
                curr[s[begin]] -= 1
                if curr[s[begin]] == 0:
                    del curr[s[begin]]
                begin += 1
        

        return max(res.values()) if res else 0