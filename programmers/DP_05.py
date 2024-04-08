# [문제 출처] - https://school.programmers.co.kr/learn/courses/30/lessons/42897
# 도둑질 (DP algorithm)


def solution(money):
    answer = 0
    
    
    n = len(money)
    
    dp1 = [-1] * (n-1)
    dp2 = [-1] * (n-1)
    dp1[0], dp1[1], dp2[0], dp2[1] = money[0], money[1], money[1], money[2]
    
    for i in range(2, n-1):
        if i == 2:
            dp1[i] = money[i] + money[0]
            dp2[i] = money[i+1] + money[1]
        else:
            dp1[i] = max(dp1[i-2], dp1[i-3]) + money[i]
            dp2[i] = max(dp2[i-2], dp2[i-3]) + money[i+1]
    
    answer = max(max(dp1), max(dp2))
    return answer