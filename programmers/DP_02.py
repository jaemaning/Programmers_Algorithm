# [문제 출처] - https://school.programmers.co.kr/learn/courses/30/lessons/43105
# 정수 삼각형 (DP algorithm)


def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if 0 < j < len(triangle[i])-1:
                triangle[i][j] = max(triangle[i][j] + triangle[i-1][j], triangle[i][j] + triangle[i-1][j-1])
            else:
                if j == 0:
                    triangle[i][j] = triangle[i][j] + triangle[i-1][j]
                else:
                    triangle[i][j] = triangle[i][j] + triangle[i-1][j-1]
            
    return max(triangle[len(triangle)-1])