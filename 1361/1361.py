class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        flag = [0 for i in range(n)]
        for ele in leftChild:
            if ele == -1:
                continue
            if flag[ele] == 0:
                flag[ele] += 1
            else:
                return False
        for ele in rightChild:
            if ele == -1:
                continue
            if flag[ele] == 0:
                flag[ele] += 1
            else:
                return False
        return sum(flag) == n-1