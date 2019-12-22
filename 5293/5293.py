class Solution:
    def checkStr(self, s, k):
        chardict = [0 for i in range(26)]
        lens = len(s)
        ret = 1
        for i in range(lens):
            chardict[ord(s[i])-ord('a')] = 1
            
        return sum(chardict) <= k
    
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        strlist = []
        maxocc = 0
        
        lens = len(s)
        for i in range(0, lens-minSize+1):
            tmps = s[i:i+minSize]
            strlist.append(tmps)
        
        strlist.sort()
        lenlist = len(strlist)
        it = 0
        
        # print(strlist)
        
        while it < lenlist:
            # print(strlist[it], self.checkStr(strlist[it], maxLetters))
            if self.checkStr(strlist[it], maxLetters):
                tmplen = 1
                it += 1
                while it<lenlist and strlist[it]==strlist[it-1]:
                    tmplen += 1
                    it += 1
                maxocc = max(maxocc, tmplen)
            else:
                it += 1
                while it<lenlist and strlist[it]==strlist[it-1]:
                    it += 1
        return maxocc
        
        
            
        