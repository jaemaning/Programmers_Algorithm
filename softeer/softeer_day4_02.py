# https://softeer.ai/class/devcrew/study/resource/detail/6280?id=155&resourceId=82
# softeer 2주 알고리즘 문제풀이 day4 - 02


import sys, math

tc = sys.stdin.readlines()

a = int(tc[0])

dp = [0 for _ in range(16)]

dp[0], dp[1] = 4, 9

for i in range(2,16):
    dp[i] = int(((math.sqrt(dp[i-1]) - math.sqrt(dp[i-2])) * 2 + math.sqrt(dp[i-1])) ** 2)

print(dp[a])