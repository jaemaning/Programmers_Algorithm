# [문제 출처] - https://programmers.co.kr/learn/courses/30/lessons/42577
# 전화번호 목록 (hash table algorithm)


def solution(phone_book):
    answer = True
    dic = {}
    
    for phone_num in phone_book:
        dic[phone_num] = 1
    
    for phone_num in phone_book:
        numbering = ""
        for i in phone_num:
            numbering += i
            if numbering in dic and numbering != phone_num:
                answer = False
                break
                
    return answer


## 공백용 ##
