# [문제 출처] - https://programmers.co.kr/learn/courses/30/lessons/42586
# 스택/큐 (Stack/Queue)


def solution(progresses, speeds):
    answer = []
    count=0

    while True:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        for i in range(len(progresses)):
            if progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                count+=1
            elif progresses[0] <100:
                if count !=0:
                    answer.append(count)
                    count=0
            if progresses == []:
                answer.append(count)
                break
            
        if progresses == []:
            break
        
                
    return answer
  
  
  ## 공백용 ##
