# https://softeer.ai/class/devcrew/study/resource/detail/6289?id=155&resourceId=81
# softeer 2주 알고리즘 문제풀이 day3 - 02

import sys

tc = sys.stdin.readlines()

N, M = map(int, tc[0].split())

users = list(map(int, tc[1].split()))
graph = [[] for _ in range(N)]
cnt = 0

for i in range(2, len(tc)):
    a, b = map(int, tc[i].split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

for i in range(N):
    flag = 1
    for j in graph[i]:
        if users[j] >= users[i]:
            flag = 0
            break

    if flag:
        cnt += 1

print(cnt)