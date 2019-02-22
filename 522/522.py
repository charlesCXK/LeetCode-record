class Solution:
    # judge if str1 is the 'substring' of str2
    def substring(self, str1, str2):
        len1, len2 = len(str1), len(str2)
        it1, it2 = 0, 0
        while it1 < len1 and it2 < len2:
            if str1[it1] == str2[it2]:
                it1 += 1
                it2 += 1
            else:
                it2 += 1
        return it1 == len1
            
    def findLUSlength(self, strs: 'List[str]') -> 'int':
        strs.sort(key=len, reverse=True)
        max_sub = -1
        
        for i in range(len(strs)):
            string = strs[i]
            length = len(string)
            
            # the length of the left string are all smaller than max_sub
            if length < max_sub:
                break
            
            for sublen in range(length, max(0, max_sub), -1):
                for start in range(0, length-sublen+1):
                    substr = string[start:start+sublen]
                    
                    flag = True
                    for j in range(0, len(strs)):
                        if i == j or len(strs[j]) < sublen:
                            continue
                        if self.substring(substr, strs[j]):
                            flag = False
                            break
                    if flag:
                        max_sub = max(max_sub, sublen)
        return max_sub