# [문제 출처] - https://programmers.co.kr/learn/courses/30/lessons/42578
# 위장 (hash table algorithm)


def solution(clothes):
    dic = {}
    count = 0
    ans = 1

    for item in clothes:
        dic[item[1]] = 0

    for item in clothes:
        if item[1] in dic:
            dic[item[1]] += 1

    for i in dic.values():
        ans *= (i+1)

    answer = ans-1
    return answer


## 공백용 ##
