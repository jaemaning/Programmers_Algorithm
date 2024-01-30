# https://softeer.ai/class/devcrew/study/resource/84?id=155
# softeer 2주 알고리즘 문제풀이 day6 - 02

import sys


def calSeat(x, y):
    minVal = 99999
    for i in range(1, N+1):
        for j in range(1, M+1):
            if res_seated[i][j]:
                minVal = min(minVal, (x-i)**2 + (y-j)**2)

    return minVal

def isValid(x, y):
    if res_seated[x][y] == 0 and res_seated[x-1][y] == 0 and res_seated[x+1][y] == 0 and res_seated[x][y-1] == 0 and res_seated[x][y+1] == 0:
        return True
    else:
        return False


def checkSeat(id):
    maxVal = 0
    for x in range(1, N+1):
        for y in range(1, M+1):
            # 좌석 체크
            if isValid(x, y):
                val = calSeat(x, y)
                if val > maxVal:
                    maxVal = val
                    id_list[id] = [x, y]

    if maxVal == 0:
        return False
    else:
        res_seated[id_list[id][0]][id_list[id][1]] = 1
        return True
                        
                    
    

tc = sys.stdin.readlines()

N, M, Q = map(int, tc[0].split())
res_seated = [[0 for _ in range(M+2)] for _ in range(N+2)]
id_list = [0 for _ in range(10002)]

for i in range(1, Q+1):
    IO, id = tc[i].split()
    id = int(id)

    if IO == "In":
        if not id_list[id]:
            if checkSeat(id):
                print(f"{id} gets the seat ({id_list[id][0]}, {id_list[id][1]}).")
            else:
                print("There are no more seats.")
        else:
            if id_list[id] == 1:
                print(f"{id} already ate lunch.")
            else:
                print(f"{id} already seated.")
    else:
        if not id_list[id]:
            print(f"{id} didn't eat lunch.")
        else:
            if id_list[id] == 1:
                print(f"{id} already left seat.")
            else:
                print(f"{id} leaves from the seat ({id_list[id][0]}, {id_list[id][1]}).")
                res_seated[id_list[id][0]][id_list[id][1]] = 0
                id_list[id] = 1
        
        

            