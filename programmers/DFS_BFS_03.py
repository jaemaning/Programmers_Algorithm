# [문제 출처] - https://school.programmers.co.kr/learn/courses/30/lessons/1844
# 게임 맵 최단거리 (DFS/BFS)

from collections import deque


def solution(maps):
    n, m = len(maps), len(maps[0])
    
    def bfs(n, m, maps):
        
        step = 0
        
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        
        visited = [[0 for _ in range(m)] for _ in range(n)]
        
        q = deque([[0, 0]])
        
        while q:
            step += 1
            for _ in range(len(q)):
                sx, sy = q.popleft()
                
                if sx == n-1 and sy == m-1:
                    return step

                for i in range(4):
                    nx = sx + dx[i]
                    ny = sy + dy[i]

                    if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] and not visited[nx][ny]:
                        q.append([nx, ny])
                        visited[nx][ny] = 1
    
    
    answer = bfs(n, m, maps)
    
    if not answer:
        answer = -1
                
    return answer