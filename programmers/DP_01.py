# [문제 출처] - https://school.programmers.co.kr/learn/courses/30/lessons/42895
# N으로 표현 (DP algorithm)


def checkDP(val, n):
    if val == None:
        return [n, -n]
    return [val + n, val - n, val * n, val // n]


def solution(N, number):
    
    if N == number:
        return 1
    
    dp = []
    dp.append([None])
    dp.append([N, -N])

    for s in range(1, 8):
        temp = []
        MULTIPLEVALUE = N
        
        for v in dp[s]:
            temp.extend(checkDP(v, N))
        
        for _ in range(s):
            MULTIPLEVALUE = MULTIPLEVALUE * 10 + N
        
        for i in range(s):
            for v in dp[i]:
                temp.extend(checkDP(v, MULTIPLEVALUE))
            MULTIPLEVALUE = MULTIPLEVALUE // 10
            
        temp = list(set(temp))
        
        if number in temp:
            return s + 1
        
        dp.append(temp)
    
    return -1
