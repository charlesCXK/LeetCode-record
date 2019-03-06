'''
Add one element to retSet one time is quicker than using set Union.
从后向前，每次保存当前元素和后面元素的所有不重复异或结果。
比如考虑 i，就拿 元素 i 和 {元素 i+1 的所有异或结果} 进行异或运算
'''
class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int: 
        retSet = set()
        res =  [set() for i in range(len(A))]
        res[-1].add(A[-1])
        retSet.add(A[-1])
        
        for i in range(len(A)-2, -1, -1):
            res[i].add(A[i])
            retSet.add(A[i])
            for element in res[i+1]:
                tmp = element | A[i]
                res[i].add(tmp)
                retSet.add(tmp)

        return len(retSet)
                