class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        out = 0
        m = len(mat)
        n = len(mat[0])
        
        for i in range(min(m,n)):
            for y in range(m-i):
                for x in range(n-i):
                    new_mat = mat[y:y+i+1]
                    s = sum([sum(l[x:x+i+1]) for l in new_mat])
                    if s <= threshold:
                        out = i + 1     # has found the solution
                        break
                if out == i + 1:
                    break
            if out != i + 1:        # if this sidelen doesn't work, the larger sidelen will not, neither.
                break
        return out