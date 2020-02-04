from itertools import combinations

N = int(input())
population = list(map(int, input().split()))
connection = {i: [j - 1 for j in list(map(int, input().split()))[1:]] for i in range(N)}


def is_connected(comb):
    check = [1 if i in comb else 0 for i in range(N)]
    visited = [0] * N
    visited[list(comb)[0]] = 1
    q = connection[list(comb)[0]]
    while q:
        nxt = []
        for i in q:
            if check[i] and not visited[i]:
                nxt += connection[i]
                visited[i] = 1
        q = set(nxt)

    for i in range(N):
        if check[i] and not visited[i]:
            return False
    else:
        return True


def diff(a, b):
    sum_a = sum([population[i] for i in a])
    sum_b = sum([population[i] for i in b])
    return abs(sum_a - sum_b)


min_ = 1e10
for k in range(1, N // 2 + 1):
    for comb in combinations(list(range(N)), k):
        a = set(comb)
        b = set(range(N)) - a
        if is_connected(a) and is_connected(b):
            min_ = min(min_, diff(a, b))

if min_ == 1e10:
    print(-1)
else:
    print(min_)
