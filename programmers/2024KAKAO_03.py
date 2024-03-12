

from collections import deque

comb_lst = []
r_dict = dict()

def bs(lst, target):
    s, e = 0, len(lst) - 1

    while s <= e:
        mid = (s+e) // 2
        if target > lst[mid]:
            s = mid + 1
        else:
            e = mid - 1
        
    return s


def comb(n, dice, lst):
    if len(lst) == n:
        comb_lst.append(lst[:])
        return
    
    s = lst[-1] + 1 if lst else 0
    for i in range(s, n*2):
            lst.append(i)
            comb(n, dice, lst)
            lst.pop()


# step : 단계, n : len(dice)//2
def sumDice(step, n, dice, a, k, cnt):
    if step == n:
        r_dict[k].append(cnt)
        return

    for i in range(6):
        sumDice(step + 1, n, dice, a, k, cnt+dice[a[step]][i])

def solution(dice):
    n = len(dice)
    comb(n//2, dice, []) # dice index 를 Combination 시켜 저장
    max_cnt = 0
    answer = []
    
    for a in comb_lst:
        k = "".join(map(str, a))
        r_dict[k] = []
        sumDice(0, n//2, dice, a, k, 0)
        r_dict[k].sort()
    
    for a in comb_lst:
        k = "".join(map(str, a))
        b = [i for i in range(n)]
        for p in a:
            b.pop(b.index(p))
        rk = "".join(map(str, b))
        
        s = 0
        cnt = 0
        l = r_dict[k]
        rl = r_dict[rk]
        for i in range(len(l)):
            cnt += bs(rl, l[i])
                    
        if max_cnt < cnt:
            max_cnt = cnt
            result = k
            
    # print(r_dict)
    for i in result:
        answer.append(int(i)+1)
    return answer
    