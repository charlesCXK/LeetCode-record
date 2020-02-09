class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[j]==arr[i]*2 and i!=j:
                    return True
        return False