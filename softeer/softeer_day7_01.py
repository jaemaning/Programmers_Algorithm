# https://softeer.ai/class/devcrew/study/resource/detail/description/6248?id=155&resourceId=85
# softeer 2주 알고리즘 문제풀이 day7 - 01


import sys

sys.setrecursionlimit(10**6)


def dfs(x, y, visited, g):

    if visited[x]:
        return
    visited[x] = 1

    for next in g[x]:
        dfs(next, y, visited, g)


tc = sys.stdin.readlines()

n, m = map(int, tc[0].split())
graph = [[] for _ in range(n+1)]
graph2 = [[] for _ in range(n+1)]

for i in range(1, m+1):
    x, y = map(int, tc[i].split())
    graph[x].append(y)
    graph2[y].append(x)

s, t = map(int, tc[-1].split())

visited_s = [0 for _ in range(n+1)]
visited_s[t] = 1
dfs(s, t, visited_s, graph)

visited_t = [0 for _ in range(n+1)]
visited_t[s] = 1
dfs(t, s, visited_t, graph)

visited_s2 = [0 for _ in range(n+1)]
dfs(s, t, visited_s2, graph2)

visited_t2 = [0 for _ in range(n+1)]
dfs(t, s, visited_t2, graph2)

result = 0
for i in range(1, n+1):
    if visited_s[i] and visited_s2[i] and visited_t[i] and visited_t2[i]:
        result += 1

print(result-2)