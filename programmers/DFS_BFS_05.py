# [문제 출처] - https://school.programmers.co.kr/learn/courses/30/lessons/87694
# 아이템 줍기 (DFS/BFS)

from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    board = [[0 for _ in range(102)] for _ in range(102)]
    
    def DrawLine(rectangle):
        nonlocal board
        
        remove_lst = []
        
        for rec in rectangle:
            for x in range(rec[0]*2,rec[2]*2+1):
                for y in range(rec[1]*2,rec[3]*2+1):
                    board[y][x] = 1

            for x in range(rec[0]*2+1,rec[2]*2):
                for y in range(rec[1]*2+1,rec[3]*2):
                    remove_lst.append([y, x])
            
        for x, y in remove_lst:
            board[x][y] = 0
            
                
    def MoveToItem(b, cx, cy, ix, iy):
        
        s = 0
        
        # 상하좌우
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        q = deque([[cx, cy]])
        b[cx][cy] = 0
        
        while q:
            s += 1
            for _ in range(len(q)):
                sx, sy = q.popleft()

                if sx == ix and sy == iy:
                    return s
                
                for i in range(4):
                    nx = sx + dx[i]
                    ny = sy + dy[i]
                    
                    if 0 <= nx < 102 and 0 <= ny < 102 and b[nx][ny]:
                        q.append([nx, ny])
                        b[nx][ny] = 0
                    
    
    DrawLine(rectangle)
    answer = MoveToItem(board, characterY*2, characterX*2, itemY*2, itemX*2)
    
    return answer //2