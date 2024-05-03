# [문제 출처] - https://school.programmers.co.kr/learn/courses/30/lessons/172927
# 프로그래머스 lv2 - 광물 캐기


def solution(picks, minerals):
    answer = 0
    
    pick_dict = {0 : "diamond", 1 : "iron", 2: "stone"}
    one_pick_dict = {
        "diamond" : {
            "diamond" : 1,
            "iron" : 1,
            "stone" : 1
        },
        "iron" : {
            "diamond" : 5,
            "iron" : 1,
            "stone" : 1
        },
        "stone" : {
            "diamond" : 25,
            "iron" : 5,
            "stone" : 1
        }
    }
    
        
    use_picks = len(minerals) // 5 +1 if len(minerals) % 5 > 0 else len(minerals) // 5
    use_picks = min(sum(picks), use_picks)
    
    pick_list = []
    
    for i in range(3):
        p = picks[i] if use_picks >= picks[i] else use_picks
        
        use_picks -= p
        for _ in range(p):
            pick_list.append(pick_dict[i])
        
        if not use_picks:
            break
            
    print(pick_list)
    minerals = [minerals[i:i+5] for i in range(0, len(minerals), 5)][:len(pick_list)]
    minerals.sort(key=lambda x : (x.count("diamond"), x.count("iron"), x.count("stone")), reverse=True)
    
    for i in range(len(minerals)):
        for mineral in minerals[i]:
            answer += one_pick_dict[pick_list[i]][mineral]
    
    
    return answer