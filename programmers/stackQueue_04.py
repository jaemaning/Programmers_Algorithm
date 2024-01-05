# [문제 출처] - https://school.programmers.co.kr/learn/courses/30/lessons/42584
# 스택/큐 (Stack/Queue)


def solution(prices):
    # 초기값 설정
    answer = [0 for _ in range(len(prices))]
    stk = []
    
    for i in range(len(prices)):
        for idx, _ in stk:
            answer[idx] += 1
        while stk and stk[-1][1] > prices[i]:
            stk.pop()
        stk.append((i, prices[i]))
    
    return answer