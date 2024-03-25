# [문제 출처] - https://school.programmers.co.kr/learn/courses/30/lessons/43238
# 입국심사 (binary search algorithm)


def solution(n, times):

    s, e = 1, max(times)*n
    while s <= e:
        mid = (s+e) // 2
        val = 0
        for t in times:
            val += mid // t
            if val >= n:
                break
        
        if val >= n:
            e = mid-1
        else:
            s = mid+1
    
    return s