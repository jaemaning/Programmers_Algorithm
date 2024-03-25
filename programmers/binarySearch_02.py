# [문제 출처] - https://school.programmers.co.kr/learn/courses/30/lessons/43236
# 입국심사 (binary search algorithm)


def solution(distance, rocks, n):
    answer = 0
    
    s = 0
    rocks.extend([0, distance])
    rocks.sort()
    nrocks = []
    
    for i in range(1, len(rocks)):
        nrocks.append(rocks[i] - rocks[i-1])
    
    s, e = 0, distance
    while s < e:
        mid = (s+e) // 2 + 1
        cnt = 0
        sumDist = 0
        for i in range(len(nrocks)):
            sumDist += nrocks[i]
            if sumDist < mid:
                cnt += 1
            else:
                sumDist = 0
                
            if cnt > n:
                e = mid - 1
                break
        else:
            s = mid

    return s