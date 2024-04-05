# https://softeer.ai/class/devcrew/study/resource/detail/submission/6250?id=155&resourceId=86
# softeer 2주 알고리즘 문제풀이 day8 - 01

import sys
from collections import deque

tc = sys.stdin.readlines()

H, K, R = map(int, tc[0].split())
a = [0]
works = [deque() for _ in range(2**H-1)]
works = a + works

for i in range(1, 2**H+1):
    work = deque(map(int, tc[i].split()))
    works.append(work)

result = 0

for i in range(1, R+1):
    for w in range(1, 2**(H+1)):
        if w == 1 and works[w]:
            result += works[w].popleft()
        elif works[w]:
            if i % 2 and w % 2:
                works[w//2].append(works[w].popleft())
            elif i % 2 == 0 and w % 2 == 0:
                works[w//2].append(works[w].popleft())

print(result) 
        