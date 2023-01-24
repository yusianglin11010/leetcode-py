# https://leetcode.com/problems/snakes-and-ladders/description/
def snakesAndLadders(board):
    need = {1:0}
    n = len(board)
    bfs = [1]
    for x in bfs:
        for i in range(x+1, x+7):
            r, c = (i-1)//n, (i-1)%n
            nxt = board[~r][c if r%2==0 else ~c]
            if nxt > 0:
                i = nxt
            if i == n*n: return need[x] + 1
            if i not in need:
                need[i] = need[x] + 1
                bfs.append(i)
    return -1