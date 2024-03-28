# [문제 출처] - https://school.programmers.co.kr/learn/courses/30/lessons/150369
# 2023 KAKAO BLIND RECRUITMENT 2번 택배 배달과 수거하기

def solution(cap, n, deliveries, pickups):
    answer = 0
    give_bag = return_bag = 0
    
    for i in range(n-1, -1, -1):
        give_bag += deliveries[i]
        return_bag += pickups[i]
        
        while give_bag > 0 or return_bag > 0:
            give_bag -= cap
            return_bag -= cap
            answer += (i + 1) * 2

    return answer