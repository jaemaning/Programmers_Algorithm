import sys

tc = sys.stdin.readlines()

room_dict = {}

N, M = map(int, tc[0].split())

for i in range(1, N+1):
    room_name = tc[i].strip()
    room_dict[room_name] = [i for i in range(9, 18)]

for j in range(N+1, len(tc)):
    r, s, t = tc[j].split()
    s, t = int(s), int(t)
    arr = room_dict[r]
    for d in range(s, t):
        arr.pop(arr.index(d))

    room_dict[r] = arr

rd = sorted(room_dict.items())

for idx in range(len(rd)):
    if idx != 0:
        print("-----")
    cnt, rem = 0, 0
    answer = []
    print(f"Room {rd[idx][0]}:")
    if rd[idx][1]:
        for time in rd[idx][1]:
            if rem:
                if time - rem == 1:
                    rem = time
                else:
                    end = rem + 1
                    answer.append("{0:02d}-{1:02d}".format(start, end))
                    rem = time
                    start = time
            else:
                rem = time
                start = time

        if start != rem:
            answer.append("{0:02d}-{1:02d}".format(start, rem+1))
        else:
            print("??", start,rem)
        
        print(str(len(answer))+" available:")
        for ans in answer:
            print(ans)
    else:
        print("Not available")
    
