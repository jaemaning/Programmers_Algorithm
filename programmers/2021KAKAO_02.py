# [문제 출처] - https://school.programmers.co.kr/learn/courses/30/lessons/81302
# 2021 KAKAO WINTER INTERNSHIP 2번 거리두기 확인하기


def solution(places):
    answer = []
    
    def CheckDist(place):
        nonlocal result
        ploc = []
        
        for i in range(len(place)):
            for j in range(len(place)):
                if place[i][j] == "P":
                    visited = [[0 for _ in range(len(place))] for _ in range(len(place))]
                    dfs(i, j, 0, [], visited, place)
                    if not result:
                        return
        
                    
        
    def dfs(x, y, s, loc, v, place):
        nonlocal result
        
        if s == 3:
            return
            
        if place[x][y] == "P" and ("O" in loc or s == 1):
            result = 0
            return
        
        # 상하좌우
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and not v[nx][ny]:
                loc.append(place[x][y])
                v[x][y] = 1
                dfs(nx, ny, s+1, loc, v, place)
                v[x][y]
                loc.pop()
            
    
    for place in places:
        result = 1
        CheckDist(place)
        answer.append(result)

    return answer