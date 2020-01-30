N = int(input())

dist = list(map(int, (input().split(" "))))
price = list(map(int, (input().split(" "))))


d = list(range(N))


d[0] = price[0] * dist[0]
min = price[0]

for i in range(1,N):
    if price[i] < min:
        min = price[i]

    if i != N-1:
        d[i] = d[i-1] + min * dist[i]
    else :
        d[i] = d[i-1]

print(d[N-1])