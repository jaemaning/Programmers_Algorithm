# https://softeer.ai/class/devcrew/study/resource/84?id=155
# softeer 2주 알고리즘 문제풀이 day6 - 01

import sys

tc = sys.stdin.readlines()

N, M = map(int, tc[0].split())

selected = [0 for _ in range(N+1)]

cnt = 0

sorting_idx_list = []
test_list = []

# sorting이 먼저 되어야할듯
for i in range(1, N+1):
    sorting_cnt = 0
    test_list.append(tc[i].rstrip())
    for j in range(1,i):
        o, t = tc[i].rstrip(), tc[j].rstrip()
        for index in range(M):
            if o[index] == t[index] or o[index] == "." or t[index] == ".":
                continue
            else:
                break
        else:
            sorting_cnt += 1

    for k in range(i+1, N+1):
        o, t = tc[i].rstrip(), tc[k].rstrip()
        for index in range(M):
            if o[index] == t[index] or o[index] == "." or t[index] == ".":
                continue
            else:
                break
        else:
            sorting_cnt += 1
    
    sorting_idx_list.append(sorting_cnt)


sorted(test_list,key=lambda sorting_idx_list:sorting_idx_list)
test_list = test_list[::-1]


for i in range(0, N):
    if not selected[i]:
        selected[i] = 1
        cnt += 1

    for j in range(i+1, N):
        if not selected[j]:
            # 선택 되지 않았다면 염기서열 비교 체크
            f, s = test_list[i], test_list[j]
            
            for k in range(M):
                if f[k] == s[k] or f[k] == "." or s[k] == ".":
                    continue
                else:
                    break
            else:
                selected[j] = 1

print(cnt)