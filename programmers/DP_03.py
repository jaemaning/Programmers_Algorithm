# [문제 출처] - https://school.programmers.co.kr/learn/courses/30/lessons/42898
# 등굣길 (DP algorithm)

def solution(m, n, puddles):
    answer = 0

    visited = [[0 for _ in range(m)] for _ in range(n)]
    rain = [[0 for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                visited[i][j] = 1
                
    for p in puddles:
        x, y = p[1]-1, p[0]-1
        if x == 0:
            for i in range(y, m):
                visited[x][i] = 0
        elif y == 0:
            for j in range(x, n):
                visited[j][y] = 0
        else:
            visited[x][y] = 0
        rain[x][y] = 1
        
    for nx in range(1, n):
        for ny in range(1, m):
            if not rain[nx][ny]:
                visited[nx][ny] = (visited[nx-1][ny] + visited[nx][ny-1]) % 1000000007
            
    return visited[n-1][m-1]