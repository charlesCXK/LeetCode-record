class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        biggerLst = [[] for i in range(n)]      # biggerLst[i] stores the index of people who is richer than i
        
        for lst in richer:
            biggerLst[lst[1]].append(lst[0])
        
        answer = [i for i in range(n)]
        leastQuiet = [quiet[i] for i in range(n)]
        
        def dfs(initInd, nowInd):
            for people in biggerLst[nowInd]:        # enumerate its neighbor nodes
                if quiet[people] < leastQuiet[initInd]:
                    leastQuiet[initInd] = quiet[people]
                    answer[initInd] = people
                
                # for people whose id is less than nowInd, we have calculated it.
                if people > nowInd:
                    dfs(initInd, people)
                else:   # use value we have calculated to update it
                    if leastQuiet[people] < leastQuiet[initInd]:
                        leastQuiet[initInd] = leastQuiet[people]
                        answer[initInd] = answer[people]
        
        for i in range(n):
            dfs(i, i)
        return answer