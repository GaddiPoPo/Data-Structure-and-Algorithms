def nqueen(n):
    col = set()
    posdiag = set()  # r+l
    negdiag = set()  # r-l
    res = []
    board = [["."]*n for i in range(n)]

    def backtrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return
        for c in range(n):
            if c in col or (r+c) in posdiag or (r-c) in negdiag:
                continue
            col.add(c)
            posdiag.add(r+c)
            negdiag.add(r-c)
            board[r][c] = "Q"

            backtrack(r+1)

            col.remove(c)
            posdiag.remove(r+c)
            negdiag.remove(r-c)
            board[r][c] = "."
    backtrack(0)
    return res
k=nqueen(4)
print(k)