# [문제 출처] - https://school.programmers.co.kr/learn/courses/30/lessons/12906
# 스택/큐 (Stack/Queue)


def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for idx in range(len(arr)):
        if idx == 0:
            answer.append(arr[idx])
        else:
            if answer[-1] != arr[idx]:
                answer.append(arr[idx])
    
    return answer