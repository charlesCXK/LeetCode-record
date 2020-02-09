class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0])
        ret = 0
        
        maxRange = (1<<n)
        # store the valid numbers in a state
        d = {x:bin(x).count('1') for x in range(maxRange)}
        
        # store the state of the classroom
        room = []
        for i in range(m):
            thisLine = 0
            for j in range(n):
                thisLine = (thisLine<<1)+(seats[i][j]=='.')
            room.append(thisLine)
        
        # dp[i][state]: the first i rows, and the i-th row is in such a state, maximum students
        dp = [[0]*maxRange for _ in range(m+1)]
        
        for i in range(1, m+1):
            for s in range(maxRange):
                # there is no adjacent in student-line, and student-line is the subset of teh room-line
                if s&(s>>1)==0 and (s&room[i-1])==s:
                    valid = d[s]    # valid number of this line
                    # enumerate the student-line of the previous row
                    for ps in range(maxRange):
                        if (ps>>1)&s==0 and (s>>1)&ps==0:       # this line and the previous line are ok
                            dp[i][s] = max(dp[i][s], dp[i-1][ps]+valid, valid)
            
                ret = max(ret, dp[i][s])
        return ret