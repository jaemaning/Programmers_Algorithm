# [문제 출처] - https://school.programmers.co.kr/learn/courses/30/lessons/1845
# 폰켓몬 (hash table algorithm)


def solution(nums):
    answer = len(nums) // 2
    
    Dnums = set(nums)
    
    answer = min(answer, len(Dnums))
    
    return answer