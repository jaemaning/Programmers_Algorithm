# [문제 출처] - https://programmers.co.kr/learn/courses/30/lessons/42587
# 프린터
# python 내장된 queue 를 사용하거나 deque 을 사용하면 시간복잡도 O(1) 로 풀이가 가능하지만,
# stack / Queue 문제는 수학적으로 충분히 생각하면 풀수 있는 문제들이 많은것 같다.


def solution(priorities, location):
    answer = 0
    count = 0
    while priorities != []:
        if priorities[0] < max(priorities):
            priorities.append(priorities[0])
            priorities.pop(0)
            location -=1
        else :
            priorities.pop(0)
            if location != count :
                answer +=1
            else :
                break
            location -=1

        if location == -1:
            location = len(priorities)-1

    answer = answer+1
    return answer
  
  
  ## 공백용 ##
