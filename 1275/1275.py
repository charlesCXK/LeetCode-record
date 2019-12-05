class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        def check(i, scores):
            for s in scores[0]:
                if s == 3:
                    return 'A'
            for s in scores[1]:
                if s == 3:
                    return 'B'

            if i == 8:
                return 'Draw'
            return 'Pending'
                
        scores = []
        scores.append([0, 0, 0, 0, 0, 0, 0, 0]) # Score for player1. row 1,2,3; col 1,2,3; left-right diagonal; riight-left diiagonal;
        scores.append([0, 0, 0, 0, 0, 0, 0, 0]) # Score for player2.
        check_flag = ''
        
        for i,m in enumerate(moves):
            row, col = m
            scores[i%2][row] += 1
            scores[i%2][col+3] += 1
            if row == col:
                scores[i%2][6] += 1
            if row+col == 2:
                scores[i%2][7] += 1
            check_flag = check(i, scores)
            if check_flag in ['A', 'B']:
                return check_flag
            
        return check_flag
        