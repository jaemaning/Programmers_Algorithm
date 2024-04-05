# https://softeer.ai/class/devcrew/study/resource/detail/submission/6250?id=155&resourceId=86
# softeer 2주 알고리즘 문제풀이 day8 - 01


import sys
from collections import defaultdict


def CheckResult(rec):

    rank_dict = defaultdict(int)
    sorted_rec = sorted(rec, reverse=True)

    for i in range(len(sorted_rec)):
        if not rank_dict[sorted_rec[i]]:
            rank_dict[sorted_rec[i]] += i + 1
            

    return rank_dict


tc = sys.stdin.readlines()

N = int(tc[0])

sum_list = [0] * N

for i in range(1, 4):
    record = list(map(int, tc[i].split()))
    for idx in range(N):
        sum_list[idx] += record[idx]
    ans = CheckResult(record)
    answer = []

    for i in range(N):
        answer.append(ans[record[i]])

    print(*answer)
    
ans = CheckResult(sum_list)
answer = []
for i in range(N):
    answer.append(ans[sum_list[i]])
print(*answer)