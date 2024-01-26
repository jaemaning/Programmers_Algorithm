# https://softeer.ai/class/devcrew/study/resource/detail/6270?id=155&resourceId=81
# softeer 2주 알고리즘 문제풀이 day3 - 01

import sys

tc = sys.stdin.readlines()

N, M = map(int, tc[0].split())

test_map = [0 for _ in range(101)]

n_location = 0

for i in range(1, N+1):
    r_dist, r_sp = map(int, tc[i].split())
    for j in range(n_location, n_location+r_dist):
        test_map[j] = r_sp

    n_location += r_dist

n_location = 0
for i in range(N+1, len(tc)):
    n_dist, n_sp = map(int, tc[i].split())
    for j in range(n_location, n_location+n_dist):
        test_map[j] = n_sp - test_map[j]

    n_location += n_dist

result = max(test_map) if max(test_map) > 0 else 0
print(result)
    