# [문제 출처] - https://school.programmers.co.kr/learn/courses/30/lessons/43163
# 단어 변환 (DFS/BFS)

from collections import deque

def CheckVal(v, w):
    cnt = 0
    l = len(v)

    for i in range(l):
        if v[i] == w[i]:
            cnt += 1
    
    if l-1 == cnt:
        return True
    else:
        return False


def solution(begin, target, words):
    answer = 0
    
    l = len(begin)
    
    def bfs(s, t, words, l):
        
        visited = [0] * 50
        q = deque([s])
        step = 0
        
        while q:
            step += 1
            for _ in range(len(q)):
                val = q.popleft()

                if val == t:
                    return step-1

                for i in range(len(words)):
                    if not visited[i] and CheckVal(val, words[i]):
                        q.append(words[i])
                        visited[i] = 1

        return 0
    
    answer = bfs(begin, target, words, l)
        
    return answer