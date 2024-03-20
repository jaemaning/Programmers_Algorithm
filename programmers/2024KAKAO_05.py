# [문제 출처] - https://school.programmers.co.kr/learn/courses/30/lessons/258705
# 2024 KAKAO WINTER INTERNSHIP 5번 산모양 타일링


def solution(n, tops):
    temp = [0] * n
    
    if tops[0]:
        dp1 = [1] + temp
        dp2 = [3] + temp
    else:
        dp1 = [1] + temp
        dp2 = [2] + temp
    
    for i in range(1, n):
        dp1[i] = (dp1[i-1] + dp2[i-1]) % 10007
        if tops[i]:
            dp2[i] = (2*dp1[i-1] + 3*dp2[i-1]) % 10007

        else:
            dp2[i] = (dp1[i-1] + 2*dp2[i-1]) % 10007

    return (dp1[n-1] + dp2[n-1]) % 10007