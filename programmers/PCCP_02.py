from collections import deque

def bfs(c, r, land, visited):
    global laneResult
    
    q = deque([(c, r)])
    visited[c][r] = 1
    
    # 상하좌우
    dc = [-1, 1, 0, 0]
    dr = [0, 0, -1, 1]
    
    cnt = 0
    land[c][r] = 0
    min_r = r
    max_r = r
    
    while q:
        cnt += 1
        c, r = q.popleft()
        min_r = min(min_r, r)
        max_r = max(max_r, r)

        for i in range(4):
            nc = c + dc[i]
            nr = r + dr[i]
            
            if 0 <= nc < len(land) and 0 <= nr < len(land[0]) and land[nc][nr] == 1 and visited[nc][nr] == 0:
                q.append((nc, nr))
                visited[nc][nr] = 1
    
    for i in range(min_r, max_r+1):
        laneResult[i] += cnt
    
    return

def solution(land):
    global laneResult
    laneResult = [0 for _ in range(len(land[0]))]
    
    visited = [[0 for _ in range(len(land[0]))] for _ in range(len(land))]
    
    for c in range(len(land)):
        for r in range(len(land[0])):
            if visited[c][r] == 0 and land[c][r] == 1:
                bfs(c, r, land, visited)
    
    
    answer = max(laneResult)

    return answer