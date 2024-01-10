# [문제 출처] - https://school.programmers.co.kr/learn/courses/30/lessons/42584
# 2024 KAKAO WINTER INTERNSHIP 1번 가장 많이 받은 선물

def solution(friends, gifts):
    answer = {}
    friendsDict = {}
    friendsGiftDict = {}
    
    for friend in friends:
        friendsDict[friend] = {}
        for nFriend in friends:
            if not nFriend == friend:
                friendsDict[friend][nFriend] = 0
        answer[friend] = 0
        friendsGiftDict[friend] = 0

    for gift in gifts:
        a, b = gift.split()
        friendsGiftDict[a] += 1
        friendsGiftDict[b] -= 1
        friendsDict[a][b] = friendsDict[a][b] + 1


    for i in friends:
        for j in friendsDict[i]:
            if friendsDict[j][i] > friendsDict[i][j]:
                answer[j] += 1
            elif friendsDict[j][i] < friendsDict[i][j]:
                answer[i] += 1
            else:
                if friendsGiftDict[i] > friendsGiftDict[j]:
                    answer[i] += 1
                elif friendsGiftDict[j] > friendsGiftDict[i]:
                    answer[j] += 1
            friendsDict[j].pop(i)
    
    result = 0
    for i in answer:
        result = max(result, answer[i])
    return result