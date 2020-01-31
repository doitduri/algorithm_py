import sys

n = int(sys.stdin.readline())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

table = [[[0]*3 for _ in range(n)] for _ in range(n)]
table[0][1][0] = 1

for x in range (2, n):
    if maps[0][x] == 0:
        table[0][x][0] = table[0][x-1][0]

for y in range(n):
    for x in range(2,n):
        if maps[y][x] == maps[y][x-1] == maps[y-1][x] == 0:
            table [y][x][2] = table[y-1][x-1][0] + table[y-1][x-1][1] + table[y-1][x-1][2]

        if maps[y][x] == 0:
            table[y][x][0] = table[y][x-1][2] + table[y][x-1][0]
            table[y][x][1] = table[y-1][x][2] + table[y-1][x][1]


print(sum(table[-1][-1]))