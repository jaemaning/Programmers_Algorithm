# https://softeer.ai/class/devcrew/study/resource/detail/6259?id=155&resourceId=82
# softeer 2주 알고리즘 문제풀이 day4 - 01


import sys


def lcs(n, m):
    cnt = 0
    dp = [[0 for _ in range(len(m)+1)] for _ in range(len(n)+1)]
    # n < m
    for i in range(1, len(n)+1):
        for j in range(1, len(m)+1):
            if n[i-1] == m[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                cnt = max(cnt, dp[i][j])
    print(cnt)
    return


tc = sys.stdin.readlines()

N, M, K = map(int, tc[0].split())

n_list = list(map(int, tc[1].split()))
m_list = list(map(int, tc[2].split()))

lcs(n_list, m_list)

