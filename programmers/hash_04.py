# [문제 출처] - https://programmers.co.kr/learn/courses/30/lessons/42579
# 베스트앨범 (hash table algorithm)


def solution(genres, plays):
    answer = []
    dic = {}
    dic2 = {}

    for gen in genres:
        dic[gen] = 0

    for gen, i in zip(genres, range(len(genres))):
        if gen in dic:
            dic[gen] += plays[i]

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        dic2[genre] = dic2.get(genre, []) + [(play, i)]

    genre_rank = sorted(dic.items(), key=lambda x: x[1],reverse=True)

    for i,total_play in genre_rank:
        play_rank = sorted(dic2[i],key=lambda x:x[0],reverse=True)
        if len(play_rank) > 2:
            rank_range = 2
        else :
            rank_range = len(play_rank)
        for j in range(rank_range):
            answer.append(play_rank[j][1])

    return answer
  
  
  ## 공백용 ##
