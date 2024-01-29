# https://softeer.ai/class/devcrew/study/resource/detail/6273?id=155&resourceId=83
# softeer 2주 알고리즘 문제풀이 day5 - 02



import sys


def perm(n_list):
    if len(m_list) == N:
        result.append(m_list[:])
        return

    for i in range(N):
        if not visited[i]:
            m_list.append(n_list[i])
            visited[i] = 1
            perm(n_list)
            visited[i] = 0
            m_list.pop()


tc = sys.stdin.readlines()

N, M, K = map(int, tc[0].split())
n_list = list(map(int, tc[1].split()))
m_list = []
result = []
visited = [0 for _ in range(N)]
perm(n_list)
ans = 99999

for arr in result:
    cnt = 0
    basket = 0
    idx = 0
    val = 0

    while cnt != K:
        if val >= ans:
            break
        
        if M >= basket + arr[idx%N]:
            basket += arr[idx%N]
            idx += 1
        else:
            val += basket
            basket = arr[idx%N]
            idx += 1
            cnt += 1

    ans = min(ans, val)
    

print(ans)