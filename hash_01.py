# 완주하지 못한 선수 (hash table algorithm)

def solution(participant, completion):
    answer = ''
    dic={}
    temp=0
    
    
    for part in participant:
        dic[hash(part)] = part
        temp += hash(part)
        
    for comp in completion:
        temp -= hash(comp)
    
    answer = dic[temp]
    
    return answer
