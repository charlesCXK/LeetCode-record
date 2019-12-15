def shortestPath(self, grid, k):
    """
    :type grid: List[List[int]]
    :type k: int
    :rtype: int
    """
   
    m = len(grid); n = len(grid[0])
    if m == 1 and n  == 1 and (grid[0][0] == 0 or k > 0):  return 0
    d = [1,0,-1,0,1]
    q = collections.deque([(0,0,k,0)])
    v = set()
    v.add((0,0,k))
    res = []
    while q:
        i,j, K, cur = q.popleft() 
        if i == m-1 and j == n-1: return cur
        for h in range(4):
            x = i + d[h]
            y = j + d[h+1]
            if x<0 or x>=m or y<0 or y>=n or (x,y,K) in v: continue
            v.add((x,y,K))
            if grid[x][y] == 1 and K>=1: q.append((x,y,K-1,cur+1))
            elif grid[x][y] == 0: q.append((x,y,K,cur+1))
    return -1