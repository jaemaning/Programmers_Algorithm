# https://softeer.ai/class/devcrew/study/resource/detail/6266?id=155&resourceId=80
# softeer 2주 알고리즘 문제풀이 day2 - 02

import sys
import heapq

tc = sys.stdin.readlines()

N, M = map(int, tc[0].split())

room_dict = {}

for i in range(1, N+1):
    room_name = tc[i].strip()
    room_dict[room_name] = []

for j in range(N+1, len(tc)):
    r, s, e = tc[j].split()
    heapq.heappush(room_dict[r], int(s))
    heapq.heappush(room_dict[r], int(e))    

rd = sorted(room_dict.items())

for i in range(len(rd)):
    # flag : 0 => room use o, flag : 1 => room use x
    n = 0
    flag = True
    start, end = 9, 18
    print(f"Room {rd[i][0]}:")
    ans = []

    while rd[i][1]:
        n = heapq.heappop(rd[i][1])
        

        if start != n and end != n and flag:
            ans.append((start, n))
            
        start = n
        flag = not flag


    if n and n != end:
        ans.append((n, end))
    elif n == 0:
        ans.append((9, 18))

    if len(ans):
        print(f"{len(ans)} available:")
        for a in range(len(ans)):
            print("{0:02d}-{1:02d}".format(ans[a][0], ans[a][1]))
    else:
        print("Not available")
    
    if i != len(rd)-1:
        print("-----")