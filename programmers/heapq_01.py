# [문제 출처] - https://school.programmers.co.kr/learn/courses/30/lessons/42626#
# 힙 (Heap)



import heapq

def solution(scoville, K):
    answer = 0
    mixed = []
    
    heapq.heapify(scoville)
    
    while scoville:
        num = heapq.heappop(scoville)
        if num >= K:
            if mixed:
                answer += 1
            break
        else:
            if not mixed:
                mixed.append(num)
            else:
                heapq.heappush(scoville, mixed[0] + num*2)
                mixed = []
                answer += 1
        
    else:
        answer = -1
    
    return answer