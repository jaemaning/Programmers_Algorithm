# [문제 출처] - https://school.programmers.co.kr/learn/courses/30/lessons/1843
# 사칙연산 (DP algorithm)


def solution(arr):
    answer = 0
    '''
    로직정리
    min_dp
    max_dp
    2가지로 구분해서 값을 구해나가야함
    '''
    INF = int(1e9)
    dp_length = len(arr)//2 + 1
    min_dp = [[INF for _ in range(dp_length)] for _ in range(dp_length)]
    max_dp = [[-INF for _ in range(dp_length)] for _ in range(dp_length)]
    
    for i in range(0, len(arr), 2):
        idx, v = i//2, int(arr[i])
        min_dp[idx][idx] = v
        max_dp[idx][idx] = v
    
    '''
    5=>10, 3=>3
    0,1 => 0,0 + 1,1 / 1, 2 => 1,1 + 2,2 / 2, 3 => 2,2 + 3,3
    '''
    for i in range(len(arr)//2):
        for j in range(i, len(arr)//2):
            x, y = j-i, j+1
            for k in range(x, y):
                if arr[2*k+1] == "+":
                    max_dp[x][y] = max(max_dp[x][y], max_dp[x][k]+max_dp[k+1][y])
                    min_dp[x][y] = min(min_dp[x][y], min_dp[x][k]+min_dp[k+1][y])
                elif arr[2*k+1] == "-":
                    max_dp[x][y] = max(max_dp[x][y], max_dp[x][k]-min_dp[k+1][y])
                    min_dp[x][y] = min(min_dp[x][y], min_dp[x][k]-max_dp[k+1][y])


    return max_dp[0][-1]
