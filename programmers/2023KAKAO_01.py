# [문제 출처] - https://school.programmers.co.kr/learn/courses/30/lessons/150370
# 2023 KAKAO BLIND RECRUITMENT 1번 개인정보 수집 유효시간


# 개인정보 수집 유효기간

def solution(today, terms, privacies):
    today_y, today_m, today_d = map(int, today.split("."))
    answer = []
    
    check_dict = dict()
    for term in terms:
        key, val = term.split()
        check_dict[key] = int(val)
        
    for i in range(len(privacies)):
        priv = privacies[i]
        date_val, type_val = priv.split()
        target_y, target_m, target_d = map(int, date_val.split("."))
        
        calc_v  = 0
        calc_v += (today_y - target_y) * 12 * 28
        calc_v += (today_m - target_m) * 28
        calc_v += (today_d - target_d)
        if check_dict[type_val] * 28 <= calc_v:
            answer.append(i+1)

        
    return answer