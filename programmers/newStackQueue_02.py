# [문제 출처] - https://school.programmers.co.kr/learn/courses/30/lessons/12909
# 스택/큐 (Stack/Queue)


def solution(s):
    answer = True
    stk = []
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i in range(len(s)):
        if len(stk) == 0:
            if s[i] == "(":
                stk.append(1)
            else:
                answer = False
                break
        else:
            if s[i] == "(":
                stk.append(1)
            else:
                stk.pop()
            
    if len(stk) != 0:
        answer = False

    return answer