# https://softeer.ai/class/devcrew/study/resource/detail/6254?id=155&resourceId=79
# softeer 2주 알고리즘 문제풀이 day1 - 02


import sys

a = sys.stdin.readlines()
result = 0

for i in range(len(a)):
    start, end = a[i].split()
    sh, sm = map(int, start.split(":"))
    eh, em = map(int, end.split(":"))
    result += (eh - sh) * 60 + (em - sm)

print(result)