# [문제 출처] - https://school.programmers.co.kr/learn/courses/30/lessons/43162
# 네트워크 (DFS/BFS)

from collections import deque


def bfs(s, visited, computers):
    
    q = deque([computers[s]])
    visited[s] = 1
    
    while q:
        c = q.popleft()

        for i in range(len(c)):
            if c[i] and not visited[i]:
                q.append(computers[i])
                visited[i] = 1
                
    return visited



def solution(n, computers):
    answer = 0
    visited = [0] * n
    
    for i in range(n):
        if not visited[i]:
            visited = bfs(i, visited, computers)
            answer += 1
    
    return answer