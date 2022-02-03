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

 ## 코드는 비슷하나 방법론 변경으로 속도단축에 있어서 압도적이길래,, 프로그래머스 익명의 고수님들의 코드를 빌려왔습니다.


from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque(0 for _ in range(bridge_length))
    total_weight = 0
    step = 0
    truck_weights.reverse()

    while truck_weights:
        total_weight -= bridge.popleft()
        if total_weight + truck_weights[-1] > weight:
            bridge.append(0)
        else:
            truck = truck_weights.pop()
            bridge.append(truck)
            total_weight += truck
        step += 1

    step += bridge_length

    return step


# 프로그래머스 임영준 , youjeongsue , 주익정 , SeungHyun Kim , 박홍균 외 5 명 풀이방법,,
