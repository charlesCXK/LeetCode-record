class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def char2int(c):
            return ord(c)-ord('0')
        
        mystr = '123456789'
        ret = []
        low = str(low)
        lenLow = len(low)
        high = str(high)
        lenHigh = len(high)
        
        ''' handle low '''
        idx = char2int(low[0])-1
        while idx+lenLow <= 9:
            nowStr = mystr[idx:idx+lenLow]
            if nowStr>=low and int(nowStr)<=int(high):
                ret.append(int(nowStr))
            idx += 1
        
        if lenHigh > lenLow:
            for nowLen in range(lenLow+1, lenHigh):
                for idx in range(0, 9-nowLen+1):
                    ret.append(int(mystr[idx:idx+nowLen]))
            idx = 0
            while idx+lenHigh <= 9:
                nowStr = mystr[idx:idx+lenHigh]
                if nowStr<=high:
                    ret.append(int(nowStr))
                idx += 1
        
        return ret