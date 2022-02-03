# [문제 출처] - https://programmers.co.kr/learn/courses/30/lessons/42586
# 스택/큐 (Stack/Queue)


from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    d1 = deque(truck_weights)
    bridge_onTrucks = [0] * bridge_length
    d2 = deque(bridge_onTrucks)


    while len(d2):
        answer += 1
        d2.popleft()
        if len(d1):
            if sum(d2) + d1[0] <= weight:
                d2.append(d1.popleft())
            else:
                d2.append(0)

    return answer

  
  ## 공백용 ##
  
  # 5번 테스트 시간초과로 실패,,
