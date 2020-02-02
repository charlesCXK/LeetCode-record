class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        import functools
        def mycmp(a, b):
            return a[1]-b[1] if a[1]!=b[1] else a[0]-b[0]
        
        m, n = len(mat), len(mat[0])
        soldierNum = []
        
        for i in range(m):
            soldier = 0
            for j in range(n):
                if mat[i][j] == 0:
                    break
                soldier += 1
            soldierNum.append((i, soldier))
        
        soldierNum.sort(key=functools.cmp_to_key(mycmp))
        
        ret = []
        for i in range(k):
            ret.append(soldierNum[i][0])
        return ret
            