# https://softeer.ai/class/devcrew/study/resource/detail/6295?id=155&resourceId=79
# softeer 2주 알고리즘 문제풀이 day1 - 01

import sys

T = sys.stdin.readlines()

for i in range(1, len(T)):
    a, b = map(int, T[i].split())
    print(f"Case #{i}: {a+b}" )
    