# [문제 출처] - https://school.programmers.co.kr/learn/courses/30/lessons/49189
# 가장 먼 노드 (그래프)


from collections import deque

def solution(n, edge):
    answer = []
    
    adjL = [[] for _ in range(n+1)]
    
    for e in edge:
        adjL[e[0]].append(e[1])
        adjL[e[1]].append(e[0])
    
        
    def bfs():
        nonlocal adjL, answer, n
        
        q = deque([1])
        visited = [0] * (n+1)
        visited[1] = 1
        
        while q:
            cnt = 0
            for _ in range(len(q)):
                s = q.popleft()
                
                for b in adjL[s]:
                    if not visited[b]:
                        q.append(b)
                        visited[b] = 1
                        cnt += 1
                        
            answer.append(cnt)
                        
    bfs()
                
    if answer[-1]:
        answer = answer[-1]
    else:
        answer = answer[-2]
        
    
    return answer