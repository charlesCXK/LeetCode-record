'''
Use binary to represent the flip operation of the first line. Then, from
the second line, colomn j, the flip operation is decided by the state of the former line, col j.
Then, calculate the state of each element in the current line according to the filp operations
of this line. Finally, if the state of the last line is all zeros, we call it a successful try.
'''
class Solution:
    import math
    # update the state of the first line.
    def updateState(self, state, n):
        it = n
        while state[it] > 1:
            state[it-1] += state[it]-1
            state[it] = 0
            it -= 1
        return state
    
    def listSum(self, board):
        ret = 0
        for list_ in board:
            ret += sum(list_)
        return ret
            
    def minFlips(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        ans = 999999
        state = [[0 for i in range(n+2)] for j in range(m+2)]
        for s in range(int(2**n)):
            # copy the matrix
            board = []      # (m+2)*(n+2)
            board.append([0 for i in range(n+2)])

            for i in range(1, m+1):
                board.append([])
                board[i].append(0)
                for j in range(1, n+1):
                    board[i].append(mat[i-1][j-1])
                board[i].append(0)

            board.append([0 for i in range(n+2)])
            
            # Handle the 1-st line. Enumerate the flip operation.
            for i in range(1, n+1):
                isFlip = (state[1][i] + state[1][i+1] + state[1][i-1]) % 2
                board[1][i] = abs(isFlip - board[1][i])
            
            for i in range(2, m+1):
                for j in range(1, n+1):
                    state[i][j] = board[i-1][j] # whether need to flip
                for j in range(1, n+1):
                    isFlip = (state[i][j-1] + state[i-1][j] + state[i][j+1] + state[i][j]) % 2
                    board[i][j] = abs(isFlip - board[i][j]) # update the state of the current element

            if sum(board[m]) == 0:
                ans = min(ans, self.listSum(state))
            
            # update the flip operation of the first line
            state[1][n] += 1
            state[1] = self.updateState(state[1], n)
        
        if ans == 999999:
            return -1
        return ans