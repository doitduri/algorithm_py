def dfs(depth):
    global n, answer, total

    if answer > 0 and answer <= depth:
        return

    if total == 0:
        if answer == -1 or answer > depth:
            answer = depth
        return

    for y in range(n):
        for x in range(n):
            if MAP[y][x]:
                break
        if MAP[y][x]:
            break;

    if MAP[y][x]:
        for size in range(1,5+1):
            if paper[size]:
                one2zero = []

            if isCoverable(y,x,size):
                for nextY in range(y, y+size):
                    for nextX in range(x,x+size):
                        MAP[nextY][nextX] = 0
                        one2zero.append((nextY, nextX))

                total -= size**(2)
                paper[size] -= 1
                dfs(depth+1)
                paper[size] += 1
                total += size**(2)

                for i in one2zero:
                    MAP[i[0]][i[1]] = 1

def isCoverable(y, x, size):
    global n
    for _y in range(y, y+size):
        for _x in range(x, x+size):
            if 0 <= _y < n and 0 <= _x <n:
                if MAP[_y][_x] == 0:
                    return False
            else :
                False

n=10
MAP = [list(map(int, input().split())) for _ in range(n)]
paper = [0]+[5]*5
answer = -1
total = sum(sum(m) for m in MAP)
dfs(0)

print(answer)