import sys

input = sys.stdin.readline

n, k = map(int,input().split())
scores = list(map(int, input().split()))

for i in range(k):
  start, end = map(int, input().split())
  result = 0
  for j in range(start-1, end):
    result += scores[j]

  answer = round(result / (end-start+1),2)
  change_answer = str(answer)
  if len(change_answer) != 5:
    change_answer += '0'
  print(change_answer)
  