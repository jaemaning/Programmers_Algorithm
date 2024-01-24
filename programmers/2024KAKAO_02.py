# [문제 출처] - https://school.programmers.co.kr/learn/courses/30/lessons/258711
# 2024 KAKAO WINTER INTERNSHIP 2번 도넛과 막대 그래프


from collections import deque

def check_loof(root, maps, max_val):
    visited = [0 for i in range(max_val+1)]
    result = [root, 0, 0, 0]
    
    for i in maps[root]:
        q = deque()
        q.append(i)
        
        while q:
            n = q.popleft()
            if visited[n]:
                # 도넛모양
                result[1] += 1
                break
            elif len(maps[n]) == 0:
                # 막대
                result[2] += 1
                break
            elif len(maps[n]) == 2:
                # 8자
                result[3] += 1
                break
            else:
                # 다음스탭
                visited[n] = 1
                q.append(maps[n][0])
                
    return result


def check_root(max_val, maps, end_dict):
    
    for i in range(1, max_val+1):
        if len(maps[i]) > 2:
            return i
        elif len(maps[i]) == 2:
            if not end_dict[i]:
                return i
    

def solution(edges):
    maps = [[] for _ in range(1000001)]
    max_val = -1
    end_dict = {i : 0 for i in range(1000001)}
    root = 0
    
    for e in edges:
        max_val = max(max_val, max(e))
        maps[e[0]].append(e[1])
        end_dict[e[1]] += 1

    maps = maps[0:max_val+1]
    
    root = check_root(max_val, maps, end_dict)
    
    result = check_loof(root, maps, max_val)
        
    return result