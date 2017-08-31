def leaderboard(rank_arr, alice_score):
    rank_list = list(set(rank_arr))
    for i in range(0, len(alice_score)):
        rank_list.append(alice_score[i])
        rank_list = sorted(rank_list, reverse=True)
        print rank_list.index(alice_score[i]) + 1

rank_arr = [100, 100, 50, 40, 40, 20, 10]
alice = [5, 25, 50, 120]

leaderboard(rank_arr, alice)