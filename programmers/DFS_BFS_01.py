# [문제 출처] - https://school.programmers.co.kr/learn/courses/30/lessons/43165
# 타겟 넘버 (DFS/BFS)


answer = 0

def recursionTargetNumberResult(Array, lastIdx, now, result, target):
    global answer
    # 탈출 조건
    if now == lastIdx:
        if result == target:
            answer += 1
        return
    
    recursionTargetNumberResult(Array, lastIdx, now + 1, result + Array[now], target)
    recursionTargetNumberResult(Array, lastIdx, now + 1, result - Array[now], target)

    
def solution(numbers, target):
    global answer
    # 재귀로 해야할듯
    recursionTargetNumberResult(numbers, len(numbers), 0, 0, target)
    myAnswer = answer
    
    return myAnswer