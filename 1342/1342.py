class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        import functools
        def mycmp(a, b):
            return a[1]-b[1]
        
        numDict = []
        lenArr = len(arr)
        arr.sort()
        
        tmpNum, tmpLen = arr[0], 1
        for i in range(1, lenArr):
            if arr[i] == arr[i-1]:
                tmpLen += 1
            else:
                numDict.append((tmpNum, tmpLen))
                tmpNum = arr[i]
                tmpLen = 1
            if i == lenArr-1:
                numDict.append((tmpNum, tmpLen))

        numDict.sort(key=functools.cmp_to_key(mycmp), reverse=True)
        s = 0
        for i in range(len(numDict)):
            s += numDict[i][1]
            if s >= lenArr // 2:
                return i+1
        