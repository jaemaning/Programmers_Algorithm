# https://softeer.ai/class/devcrew/study/resource/detail/6271?id=155&resourceId=83
# softeer 2주 알고리즘 문제풀이 day5 - 01


import sys
from collections import deque


# 태범이 이동이 먼저
# 그다음 소나기 이동
# 소나기가 태범이 위치면 out 이지만 태범이가 골인한 순간 종료

def bfs(gini_maps, start, rain, R, C):
    # 상하좌우
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]

    q = deque([start])
    rq = deque(rain)
    cnt = 0

    while q:
        cnt += 1
        for _ in range(len(q)):
            sy, sx = q.popleft()
            visited[sy][sx] = 1
    
            for i in range(4):
                nx = sx + dx[i]
                ny = sy + dy[i]
                if 0 <= ny < R and 0 <= nx < C and visited[ny][nx] == 0:
                    # 집일경우
                    if gini_maps[ny][nx] == "H":
                        return cnt
                    # 강이나 비가오는 지역일 경우
                    elif gini_maps[ny][nx] == "*" or gini_maps[ny][nx] == "X":
                        continue
                    # 이동 가능한 경우
                    elif gini_maps[ny][nx] == ".":
                        visited[ny][nx] = 1
                        q.append([ny, nx])
                        gini_maps[ny][nx] = "W"

        for _ in range(len(rq)):
            rsy, rsx = rq.popleft()
            r_visited[rsy][rsx] = 1

            for j in range(4):
                nsy = rsy + dy[j]
                nsx = rsx + dx[j]
                if 0 <= nsy < R and 0 <= nsx < C and r_visited[nsy][nsx] == 0:
                    # 집일 경우
                    if gini_maps[nsy][nsx] == "H":
                        continue
                    # 길일 경우
                    elif gini_maps[nsy][nsx] == ".":
                        gini_maps[nsy][nsx] = "*"
                        rq.append((nsy, nsx))
                        r_visited[nsy][nsx] = 1
                    # 강일 경우
                    elif gini_maps[nsy][nsx] == "X":
                        continue
                    # 차가 있을지도 모를 경우
                    elif gini_maps[nsy][nsx] == "W":
                        gini_maps[nsy][nsx] = "*"
                        if [nsy, nsx] in q:
                            del q[q.index([nsy, nsx])]
                            
    return "FAIL"

tc = sys.stdin.readlines()

R, C = map(int,tc[0].split())
gini_maps = [[] for _ in range(R)]
rain = []
visited = [[0 for _ in range(C)] for _ in range(R)]
r_visited = [[0 for _ in range(C)] for _ in range(R)]

for i in range(1, len(tc)):
    for j in range(C):
        gini_maps[i-1].append(tc[i][j])
        if tc[i][j] == "W":
            start = (i-1, j)
            visited[i-1][j] = 1
        elif tc[i][j] == "*":
            rain.append([i-1, j])
            r_visited[i-1][j] = 1

ans = bfs(gini_maps, start, rain, R, C)
print(ans)
