# [문제 출처] - https://school.programmers.co.kr/learn/courses/30/lessons/150368
# 2023 KAKAO BLIND RECRUITMENT 3번 이모티콘 할인행사


def solution(users, emoticons):
    e_values = []
    discount_val = [10, 20, 30, 40]
    # 이모티콘 할인율은 10, 20, 30, 40 고정
    
    def perm(temp, n):
        # 이모티콘 플러스 서비스 가입자를 최대한 늘리기
        nonlocal e_values, emoticons, discount_val
        
        if len(temp) == n:
            # 바로 확인하자
            people, price = 0, 0
            
            for user in users:
                userPrice = 0
                for idx in range(len(temp)):
                    if temp[idx] >= user[0]:
                        userPrice += int(emoticons[idx] * (100-temp[idx]) / 100)
                        
                    if userPrice >= user[1]:
                        people += 1
                        break
                else:
                    price += userPrice
                        
            e_values.append([people, price])
            return
        
        for i in range(4):
            temp.append(discount_val[i])
            perm(temp, n)
            temp.pop()
    
    
    perm([], len(emoticons))
    e_values.sort(key=lambda x : [x[0], x[1]])

    return e_values[-1]