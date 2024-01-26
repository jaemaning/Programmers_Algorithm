# https://softeer.ai/class/devcrew/study/resource/detail/6288?id=155&resourceId=80
# softeer 2주 알고리즘 문제풀이 day2 - 01


import sys

t = sys.stdin.readlines()

W, N = map(int, t[0].split())
b = [0 for i in range(10**4 + 1)]
result = 0

for i in range(1, len(t)):
    M, P = map(int, t[i].split())
    b[P] += M

for price in range(len(b)-1, 0, -1):
    if price:
        if W >= b[price]:
            result += b[price] * price
            W -= b[price]
        else:
            result += W * price
            break
        
print(result)
    