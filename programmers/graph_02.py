# [문제 출처] - https://school.programmers.co.kr/learn/courses/30/lessons/49191
# 순위 (그래프)

def solution(n, results):
    answer = 0
    adjll = [[] for _ in range(n+1)]
    adjlw = [[] for _ in range(n+1)]
    
    for w, l in results:
        adjlw[w].append(l)
        adjll[l].append(w)

    
    def CheckFront(t):
        nonlocal adjll, visited, cnt
        
        for node in adjll[t]:
            if not visited[node]:
                cnt += 1
                visited[node] = 1
                CheckFront(node)
        
        return
    
    
    def CheckBack(t):
        nonlocal adjlw, visited, cnt
        
        for node in adjlw[t]:
            if not visited[node]:
                cnt += 1
                visited[node] = 1
                CheckBack(node)
        
        return
    
    
    for i in range(n+1):
        visited = [0] * (n+1)
        cnt = 0
        CheckFront(i)
        CheckBack(i)
        if cnt == n-1:
            answer += 1

    return answer