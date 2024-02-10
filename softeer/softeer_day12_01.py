import sys
from collections import deque


def isValid(nx, ny, n):
    if 0 <= nx < n and 0 <= ny < n:
        return True
    else:
        return False



def bfs(n, now, time, d_list):

    # direction 2번 index 하우상좌(0,1,2,3)
    q = deque([[0, 0, 2]])
    # 방문 확인은 할 필요없음 방문으로 추후 체크만
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[0][0] = 1

    # 하우상좌 세팅
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while q and now < time:
        for _ in range(len(q)):
            x, y, d = q.popleft()
            isd = d_list[x][y][now]
            # direction 과 n 이 맞는지 확인
            if isd % 4 == d:
                for i in d_dict[isd]:
                    nx = x + dx[i]
                    ny = y + dy[i]
                    nd = i
                    if isValid(nx, ny, n):
                        q.append([nx, ny, nd])
                        visited[nx][ny] = 1
                
        now += 1
            
    return visited



input = sys.stdin.readline

N, T = map(int, input().split())
d_dict = {
    1 : [0, 1, 2], # 상 우 하
    2 : [1, 2, 3], # 좌 상 우
    3 : [0, 2, 3], # 상 좌 하
    4 : [0, 1, 3], # 좌 하 우
    5 : [1, 2], # 상 우
    6 : [2, 3], # 좌 상
    7 : [0, 3], # 좌 하
    8 : [0, 1], # 하 우
    9 : [0, 1], # 우 하
    10 : [1, 2], # 상 우
    11 : [2, 3], # 좌 상
    12 : [0, 3], # 좌 하
}

time = 0
d_list = [[] for _ in range(N)]

for i in range(N):
    for _ in range(N):
        N_list = list(map(int, input().split()))
        d_list[i].append(N_list)


result = bfs(N, 0, T, d_list)
ans = 0

for i in range(N):
    ans += sum(result[i])

print(ans)