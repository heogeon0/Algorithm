from collections import deque
delta = [(-1,0), (1,0), (0,-1), (0,1)]
opp = {
    'S' : [0,1,2,3],
    'L' : [2,3,1,0],
    'R' : [3,2,0,1]
}

def solution(grid):
    def lazer(sr, sc, d):
        nonlocal v, answer
        if str(d) not in v[sr][sc]:
            v[sr][sc] += str(d)
            answer.append(1)

            Q = deque([[sr, sc, d]])

            while Q:
                rr, cc, nd = Q.popleft()

                dd = opp[grid[rr][cc]]
                x, y = delta[dd[nd]]

                dx, dy = rr + x, cc + y
                if dx < 0: dx = nr - 1
                if dx >= nr: dx = 0
                if dy < 0: dy = nc - 1
                if dy >= nc: dy = 0

                if str(dd[nd]) not in v[dx][dy]:
                    answer[-1] += 1
                    v[dx][dy] += str(dd[nd])
                    Q.append([dx,dy,dd[nd]])

        else:
            return

    nr = len(grid)
    nc = len(grid[0])
    v = [[''] * nc for _ in range(nr)]
    answer = []

    for i in range(nr):
        for j in range(nc):
            for d in range(4):
                lazer(i,j,d)
    answer.sort()
    return answer

print(solution(["SL","LR"]))