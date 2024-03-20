# [문제 출처] - https://school.programmers.co.kr/learn/courses/30/lessons/258707
# 2024 KAKAO WINTER INTERNSHIP 4번 n + 1 카드게임


def solution(coin, cards):
    answer = 0
    
    n = len(cards)
    target = n + 1
    
    hand = cards[:n//3]
    wish = cards[n//3:n//3+2]
    cards = cards[n//3+2:]
    flag = 1
    min_v = (n // 6) * 2 + 1
    
    while flag:
        for i in range(len(hand)):
            t = target - hand[i]
            if t in hand:
                print("??")
                answer += 1
                new_card = cards[:2]
                cards = cards[2:]
                wish = wish + new_card
                hand.pop(i)
                hand.pop(hand.index(t))
                break
                
            elif t in wish:
                if coin > 0:
                    answer += 1
                    coin -= 1
                    new_card = cards[:2]
                    cards = cards[2:]
                    wish = wish + new_card
                    hand.pop(i)
                    wish.pop(wish.index(t))
                    break
        
        else:
            for j in range(len(wish)):
                t = target - wish[j]
                if t in wish and coin > 1:
                    answer += 1
                    coin -= 2
                    wish.pop(j)
                    wish.pop(wish.index(t))
                    new_card = cards[:2]
                    cards = cards[2:]
                    wish = wish + new_card
                    break
            else:
                flag = 0
                        
    return min(answer + 1, min_v)
