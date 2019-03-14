class Solution:
    retStr = []
    
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.retStr = []
        
        '''
        parameters:
            s: string
            ind: index in s
            nowVal: how many '(' that haven't beed matched until index ind.
            nowStr: string formed until now.
            n: length of s
        '''
        def dfs(s, ind, nowVal, nowStr, n):
            '''
            We have traversal the whole string. Check whether it is valid (nowVal==0), and only keep the longest one in the result array
            '''
            
            # pruning
            if nowVal > n-ind:
                return
            
            if ind==n:
                if nowVal==0:
                    if len(self.retStr)==0 or (len(nowStr)==len(self.retStr[0]) and nowStr not in self.retStr):
                        self.retStr.append(nowStr)
                    else:
                        if len(nowStr) > len(self.retStr[0]):
                            self.retStr = []
                            self.retStr.append(nowStr)
                return
            
            if not s[ind]==')' and not s[ind]=='(':
                dfs(s, ind+1, nowVal, nowStr+s[ind], n)
            elif s[ind] == '(':
                dfs(s, ind+1, nowVal+1, nowStr+'(', n)     # select this '('
                dfs(s, ind+1, nowVal, nowStr, n)       # don't select
            else:
                if nowVal > 0:
                    dfs(s, ind+1, nowVal-1, nowStr+')', n)
                dfs(s, ind+1, nowVal, nowStr, n)

        
        dfs(s, 0, 0, '', len(s))
        if len(self.retStr) == 0:
            return [""]
        return self.retStr
        